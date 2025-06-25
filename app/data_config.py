#!/usr/bin/env python3
"""
Yarr! Data configuration and management for our analytics treasure chest
This be where we define different data sources and their schemas, matey!
Enhanced to handle multiple zip files automatically like a proper data pirate!
"""

import os
import pandas as pd
import zipfile
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataSource:
    """
    Configuration for a data source - like a treasure map for each dataset!
    """

    name: str
    description: str
    file_path: str
    schema_file: Optional[str] = None
    primary_columns: List[str] = None
    date_columns: List[str] = None
    categorical_columns: List[str] = None

    def __post_init__(self):
        """Yarr! Set up default values after initialization"""
        if self.primary_columns is None:
            self.primary_columns = []
        if self.date_columns is None:
            self.date_columns = []
        if self.categorical_columns is None:
            self.categorical_columns = []


class DataManager:
    """
    Yarr! The master of all data treasures - handles loading, validation, and analysis
    Automatically extracts zip files and manages multiple data sources like a seasoned pirate!
    """

    def __init__(self, base_data_path: str):
        self.base_data_path = Path(base_data_path)
        self.data_sources = {}
        self._ensure_data_extracted()
        self._setup_data_sources()

    def _ensure_data_extracted(self):
        """
        Yarr! Automatically extract any zip files found in the data directory
        This be our treasure extraction process for compressed data sources!
        """
        if not self.base_data_path.exists():
            return

        # Find all zip files in the data directory
        zip_files = list(self.base_data_path.glob("*.zip"))

        for zip_file in zip_files:
            # Create extraction directory name (remove .zip extension)
            extract_dir = self.base_data_path / zip_file.stem

            # Only extract if directory doesn't exist or is empty
            if not extract_dir.exists() or not any(extract_dir.iterdir()):
                try:
                    print(f"🏴‍☠️ Extracting data treasure from {zip_file.name}...")

                    # Create extraction directory
                    extract_dir.mkdir(exist_ok=True)

                    # Extract the zip file
                    with zipfile.ZipFile(zip_file, "r") as zip_ref:
                        zip_ref.extractall(extract_dir)

                    print(
                        f"✓ Successfully extracted {zip_file.name} to {extract_dir.name}/"
                    )

                except Exception as e:
                    print(f"⚠️ Warning: Failed to extract {zip_file.name}: {str(e)}")
                    continue

    def _discover_data_sources(self):
        """
        Yarr! Automatically discover data sources from extracted directories
        This makes adding new data sources as easy as dropping a zip file!
        """
        discovered_sources = {}

        # Look for extracted directories
        for item in self.base_data_path.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                # Look for CSV files in the directory
                csv_files = list(item.glob("*.csv"))

                if csv_files:
                    # Check for common survey data patterns
                    main_data_file = None
                    schema_file = None

                    for csv_file in csv_files:
                        if "schema" in csv_file.name.lower():
                            schema_file = csv_file
                        elif (
                            "results" in csv_file.name.lower()
                            or "survey" in csv_file.name.lower()
                        ):
                            # Yarr! Prefer non-schema files for main data
                            if (
                                main_data_file is None
                                or csv_file.stat().st_size
                                > main_data_file.stat().st_size
                            ):
                                main_data_file = csv_file

                    # If no obvious main file, use the largest CSV
                    if not main_data_file and csv_files:
                        main_data_file = max(csv_files, key=lambda f: f.stat().st_size)

                    if main_data_file:
                        discovered_sources[item.name] = {
                            "data_file": main_data_file,
                            "schema_file": schema_file,
                            "all_files": csv_files,
                        }

        return discovered_sources

    def _setup_data_sources(self):
        """
        Set up data sources by discovering them automatically and configuring known ones
        This be the treasure cataloging process!
        """
        discovered = self._discover_data_sources()

        # Configure Stack Overflow 2023 Survey if found
        if "kaggle_so_2023_data" in discovered:
            so_2023 = discovered["kaggle_so_2023_data"]
            self.register_data_source(
                DataSource(
                    name="stackoverflow_2023",
                    description="Stack Overflow Developer Survey 2023 - The complete dataset of developer insights",
                    file_path=str(so_2023["data_file"]),
                    schema_file=(
                        str(so_2023["schema_file"]) if so_2023["schema_file"] else None
                    ),
                    primary_columns=[
                        "LanguageHaveWorkedWith",
                        "LanguageWantToWorkWith",
                        "DatabaseHaveWorkedWith",
                        "DatabaseWantToWorkWith",
                        "PlatformHaveWorkedWith",
                        "PlatformWantToWorkWith",
                        "WebframeHaveWorkedWith",
                        "WebframeWantToWorkWith",
                    ],
                    categorical_columns=[
                        "Country",
                        "Employment",
                        "DevType",
                        "EdLevel",
                        "YearsCode",
                        "YearsCodePro",
                        "OrgSize",
                    ],
                )
            )

        # Auto-configure other discovered data sources with generic settings
        for dir_name, files_info in discovered.items():
            if dir_name not in ["kaggle_so_2023_data"]:  # Skip already configured ones
                # Try to detect common column patterns by loading a sample
                try:
                    sample_df = pd.read_csv(files_info["data_file"], nrows=1)
                    columns = list(sample_df.columns)

                    # Look for technology-related columns (semicolon-separated patterns)
                    tech_columns = []
                    for col in columns:
                        col_lower = col.lower()
                        if any(
                            tech_word in col_lower
                            for tech_word in [
                                "language",
                                "database",
                                "platform",
                                "framework",
                                "tool",
                                "tech",
                            ]
                        ):
                            tech_columns.append(col)

                    # Register the discovered data source
                    source_name = dir_name.lower().replace("-", "_").replace(" ", "_")
                    self.register_data_source(
                        DataSource(
                            name=source_name,
                            description=f"Auto-discovered data source: {dir_name}",
                            file_path=str(files_info["data_file"]),
                            schema_file=(
                                str(files_info["schema_file"])
                                if files_info["schema_file"]
                                else None
                            ),
                            primary_columns=tech_columns[
                                :8
                            ],  # Limit to first 8 technology columns
                            categorical_columns=[],  # Would need more analysis to determine
                        )
                    )

                    print(f"🏴‍☠️ Auto-registered data source: {source_name}")
                    if tech_columns:
                        print(
                            f"   └─ Found {len(tech_columns)} potential technology columns"
                        )

                except Exception as e:
                    print(f"⚠️ Could not auto-configure {dir_name}: {str(e)}")
                    continue

    def register_data_source(self, data_source: DataSource):
        """Register a new data source for analysis"""
        self.data_sources[data_source.name] = data_source

    def get_available_sources(self) -> Dict[str, str]:
        """Get all available data sources and their descriptions"""
        return {name: source.description for name, source in self.data_sources.items()}

    def load_data(self, source_name: str) -> pd.DataFrame:
        """
        Load data from a specified source with proper error handling
        """
        if source_name not in self.data_sources:
            raise ValueError(f"Arrr! Unknown data source: {source_name}")

        source = self.data_sources[source_name]

        if not os.path.exists(source.file_path):
            raise FileNotFoundError(
                f"Shiver me timbers! Data file not found: {source.file_path}"
            )

        try:
            # Load the main data
            df = pd.read_csv(source.file_path)

            # Load schema information if available
            if source.schema_file and os.path.exists(source.schema_file):
                schema_df = pd.read_csv(source.schema_file)
                # Store schema info as metadata (could be used for validation)
                df.attrs["schema"] = schema_df

            return df

        except Exception as e:
            raise RuntimeError(
                f"Blimey! Error loading data from {source.file_path}: {str(e)}"
            )

    def get_schema_info(self, source_name: str) -> Optional[pd.DataFrame]:
        """Get schema information for a data source if available"""
        if source_name not in self.data_sources:
            return None

        source = self.data_sources[source_name]
        if source.schema_file and os.path.exists(source.schema_file):
            return pd.read_csv(source.schema_file)
        return None

    def analyze_technology_usage(
        self, source_name: str, technology_column: str, top_n: int = 10
    ) -> Dict[str, List]:
        """
        Analyze technology usage from semicolon-separated data
        This be the core analysis function that can work with different technology columns
        """
        df = self.load_data(source_name)

        if technology_column not in df.columns:
            raise ValueError(
                f"Column '{technology_column}' not found in dataset. Available columns with technology data: {self.data_sources[source_name].primary_columns}"
            )

        # Count technologies (handling semicolon-separated values)
        tech_counts = {}

        for tech_str in df[technology_column].dropna():
            if pd.isna(tech_str) or tech_str == "":
                continue

            # Split by semicolon and clean up each technology name
            technologies = [
                tech.strip() for tech in str(tech_str).split(";") if tech.strip()
            ]

            for tech in technologies:
                tech_counts[tech] = tech_counts.get(tech, 0) + 1

        # Sort and get top N
        sorted_techs = sorted(tech_counts.items(), key=lambda x: x[1], reverse=True)[
            :top_n
        ]

        return {
            "labels": [tech[0] for tech in sorted_techs],
            "values": [tech[1] for tech in sorted_techs],
            "total_responses": len(df[technology_column].dropna()),
            "unique_technologies": len(tech_counts),
        }

    def get_available_analysis_columns(self, source_name: str) -> List[str]:
        """Get columns available for technology analysis"""
        if source_name not in self.data_sources:
            return []
        return self.data_sources[source_name].primary_columns

    def get_data_source_info(self, source_name: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a data source"""
        if source_name not in self.data_sources:
            return None

        source = self.data_sources[source_name]
        return {
            "name": source.name,
            "description": source.description,
            "file_path": source.file_path,
            "has_schema": source.schema_file is not None,
            "primary_columns": source.primary_columns,
            "categorical_columns": source.categorical_columns,
            "file_exists": os.path.exists(source.file_path),
        }


# Global data manager instance
data_manager = DataManager(os.path.join(os.path.dirname(__file__), "..", "data"))
