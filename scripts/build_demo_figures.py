#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"

COPPER = "#B35A1F"
COPPER_DARK = "#7D3D16"
BLUE = "#3C6E9C"
GRAY = "#B7B7B7"
GRAY_DARK = "#666666"
GRID = "#E6E6E6"


def save_all(fig: plt.Figure, stem: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ext in ["png", "pdf", "svg"]:
        kwargs = {"bbox_inches": "tight"}
        if ext == "png":
            kwargs["dpi"] = 320
        fig.savefig(OUT / f"{stem}.{ext}", **kwargs)
    plt.close(fig)


def figure1_share_exposure() -> None:
    df = pd.read_csv(DATA / "figure1_production_geography_source_data.csv")
    df = df[df["panel"] == "b_scatter"].copy()
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    colors = df["tier_status"].map({"direct": COPPER, "proxy": BLUE, "warning": GRAY}).fillna(GRAY)
    sizes = 80 + df["contribution"].fillna(0) * 4200
    ax.scatter(df["production_share_pct"], df["country_exposure"], s=sizes, c=colors, edgecolor="white", linewidth=0.7)
    for _, row in df.nlargest(5, "contribution").iterrows():
        ax.text(row["production_share_pct"] + 0.3, row["country_exposure"], row["country"], fontsize=8)
    ax.set_xlabel("Production share (%)")
    ax.set_ylabel("Country exposure")
    ax.set_title("Figure 1 demo: share versus exposure")
    ax.grid(True, color=GRID, linewidth=0.7)
    save_all(fig, "Figure_1_Share_Exposure_Scatter_Demo")


def figure2_cpwe_gli_coverage() -> None:
    df = pd.read_csv(DATA / "figure2_cpwe_gli_coverage_source_data.csv")
    cpwe = df[df["panel"] == "a_cpwe"].copy()
    gli = df[df["panel"] == "b_cpwe_vs_gli"].copy()
    cov = df[df["panel"] == "c_coverage"].copy()
    metals = ["Copper", "Lead", "Zinc", "Tin", "Aluminium", "Nickel"]
    palette = {m: (COPPER if m == "Copper" else GRAY) for m in metals}
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 4.0))
    for metal in metals:
        sub = cpwe[cpwe["metal"] == metal].sort_values("buffer_km")
        axes[0].plot(sub["buffer_km"], sub["CPWE_after_observed_upgrade"], marker="o", color=palette[metal], linewidth=2 if metal == "Copper" else 1)
        if not sub.empty:
            axes[0].text(sub["buffer_km"].max() + 2, sub["CPWE_after_observed_upgrade"].iloc[-1], metal, fontsize=7, color=palette[metal])
    axes[0].set_xlabel("Buffer (km)")
    axes[0].set_ylabel("CPWE")
    axes[0].set_title("CPWE across buffers")
    axes[0].grid(True, color=GRID, linewidth=0.7)
    axes[0].set_xlim(45, 215)

    axes[1].scatter(gli["CPWE_after_observed_upgrade"], gli["GLI_after_observed_upgrade"], s=180, c=gli["metal"].map(palette))
    for _, row in gli.iterrows():
        axes[1].text(row["CPWE_after_observed_upgrade"] + 0.003, row["GLI_after_observed_upgrade"], row["metal"], fontsize=7)
    axes[1].set_xlabel("CPWE at 100 km")
    axes[1].set_ylabel("GLI at 100 km")
    axes[1].set_title("CPWE versus GLI")
    axes[1].grid(True, color=GRID, linewidth=0.7)

    for metal in metals:
        sub = cov[cov["metal"] == metal].sort_values("buffer_km")
        axes[2].plot(sub["buffer_km"], sub["observed_or_background_share"], marker="o", color=palette[metal], linewidth=2 if metal == "Copper" else 1)
    axes[2].axhline(0.8, color=GRAY_DARK, linestyle="--", linewidth=1)
    axes[2].set_xlabel("Buffer (km)")
    axes[2].set_ylabel("Observed/background share")
    axes[2].set_title("Coverage gate")
    axes[2].grid(True, color=GRID, linewidth=0.7)
    axes[2].set_xlim(45, 215)
    save_all(fig, "Figure_2_CPWE_GLI_Coverage_Demo")


def figure3_top_country() -> None:
    df = pd.read_csv(DATA / "figure3_top_country_contribution_source_data.csv")
    track = df[(df["panel"] == "a_three_track") & (df["buffer_km"] == 100)].copy()
    track = track.sort_values("contribution", ascending=True)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1.15, 1]})
    axes[0].barh(track["country"], track["contribution"], color=[COPPER if x == "current_same_metal_country" else BLUE if "mrds" in str(x) else GRAY for x in track["exposure_source_tier"]])
    axes[0].set_xlabel("Contribution to CPWE")
    axes[0].set_title("Top-country contribution at 100 km")
    axes[0].grid(True, axis="x", color=GRID, linewidth=0.7)

    axes[1].scatter(track["global_share"] * 100, track["country_exposure"], s=120, color=COPPER_DARK)
    for _, row in track.iterrows():
        axes[1].text(row["global_share"] * 100 + 0.3, row["country_exposure"], row["country"], fontsize=7)
    axes[1].set_xlabel("Production share (%)")
    axes[1].set_ylabel("Country exposure")
    axes[1].set_title("Share versus exposure")
    axes[1].grid(True, color=GRID, linewidth=0.7)
    save_all(fig, "Figure_3_Top_Country_Contribution_Demo")


def figure4_controls() -> None:
    df = pd.read_csv(DATA / "figure4_controls_source_data.csv")
    loo = df[df["panel"] == "a_leave_one_country_out"].copy().sort_values("abs_effect", ascending=True)
    shuf = df[df["panel"] == "b_shuffle_null_summary"].copy().sort_values("buffer_km")
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8))
    axes[0].barh(loo["country_display"], loo["relative_change"], color=COPPER)
    axes[0].axvline(-0.25, color=GRAY_DARK, linestyle="--", linewidth=1)
    axes[0].axvline(0.25, color=GRAY_DARK, linestyle="--", linewidth=1)
    axes[0].set_xlabel("Relative change after removal")
    axes[0].set_title("Leave-one-country-out")
    axes[0].grid(True, axis="x", color=GRID, linewidth=0.7)

    axes[1].errorbar(shuf["buffer_km"], shuf["null_mean"], yerr=shuf["null_sd"], fmt="o-", color=BLUE, label="Null mean ± sd")
    axes[1].scatter(shuf["buffer_km"], shuf["observed_CPWE"], color=COPPER_DARK, s=70, label="Observed")
    axes[1].set_xlabel("Buffer (km)")
    axes[1].set_ylabel("CPWE")
    axes[1].set_title("Shuffle summary")
    axes[1].grid(True, color=GRID, linewidth=0.7)
    axes[1].legend(frameon=False, fontsize=8)
    save_all(fig, "Figure_4_Controls_Demo")


def main() -> None:
    figure1_share_exposure()
    figure2_cpwe_gli_coverage()
    figure3_top_country()
    figure4_controls()
    print(f"Demo figures written to: {OUT}")


if __name__ == "__main__":
    main()
