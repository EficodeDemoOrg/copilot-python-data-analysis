#!/usr/bin/env python3
"""
Yarr! Data configuration and management for our analytics treasure chest
This be where we define different data sources and their schemas, matey!
"""

import os
import pandas as pd
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
    """
    
    def __init__(self, base_data_path: str):
        self.base_data_path = Path(base_data_path)
        self.data_sources = {}
        self._setup_default_sources()
    
    def _setup_default_sources(self):
        """Set up the default data sources we know about"""
        
        # Stack Overflow 2023 Survey - our main treasure!
        so_2023_path = self.base_data_path / "kaggle_so_2023" / "survey_results_public.csv"
        so_2023_schema_path = self.base_data_path / "kaggle_so_2023" / "survey_results_schema.csv"
        
        self.register_data_source(DataSource(
            name="stackoverflow_2023",
            description="Stack Overflow Developer Survey 2023 - The complete dataset of developer insights",
            file_path=str(so_2023_path),
            schema_file=str(so_2023_schema_path) if so_2023_schema_path.exists() else None,
            primary_columns=[
                "LanguageHaveWorkedWith", "LanguageWantToWorkWith", 
                "DatabaseHaveWorkedWith", "DatabaseWantToWorkWith",
                "PlatformHaveWorkedWith", "PlatformWantToWorkWith",
                "WebframeHaveWorkedWith", "WebframeWantToWorkWith"
            ],
            categorical_columns=[
                "Country", "Employment", "DevType", "EdLevel", 
                "YearsCode", "YearsCodePro", "OrgSize"
            ]
        ))
    
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
            raise FileNotFoundError(f"Shiver me timbers! Data file not found: {source.file_path}")
        
        try:
            # Load the main data
            df = pd.read_csv(source.file_path)
            
            # Load schema information if available
            if source.schema_file and os.path.exists(source.schema_file):
                schema_df = pd.read_csv(source.schema_file)
                # Store schema info as metadata (could be used for validation)
                df.attrs['schema'] = schema_df
            
            return df
            
        except Exception as e:
            raise RuntimeError(f"Blimey! Error loading data from {source.file_path}: {str(e)}")
    
    def get_schema_info(self, source_name: str) -> Optional[pd.DataFrame]:
        """Get schema information for a data source if available"""
        if source_name not in self.data_sources:
            return None
        
        source = self.data_sources[source_name]
        if source.schema_file and os.path.exists(source.schema_file):
            return pd.read_csv(source.schema_file)
        return None
    
    def analyze_technology_usage(self, source_name: str, technology_column: str, top_n: int = 10) -> Dict[str, List]:
        """
        Analyze technology usage from semicolon-separated data
        This be the core analysis function that can work with different technology columns
        """
        df = self.load_data(source_name)
        
        if technology_column not in df.columns:
            raise ValueError(f"Column '{technology_column}' not found in dataset. Available columns with technology data: {self.data_sources[source_name].primary_columns}")
        
        # Count technologies (handling semicolon-separated values)
        tech_counts = {}
        
        for tech_str in df[technology_column].dropna():
            if pd.isna(tech_str) or tech_str == '':
                continue
            
            # Split by semicolon and clean up each technology name
            technologies = [tech.strip() for tech in str(tech_str).split(';') if tech.strip()]
            
            for tech in technologies:
                tech_counts[tech] = tech_counts.get(tech, 0) + 1
        
        # Sort and get top N
        sorted_techs = sorted(tech_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
        
        return {
            "labels": [tech[0] for tech in sorted_techs],
            "values": [tech[1] for tech in sorted_techs],
            "total_responses": len(df[technology_column].dropna()),
            "unique_technologies": len(tech_counts)
        }
    
    def get_available_analysis_columns(self, source_name: str) -> List[str]:
        """Get columns available for technology analysis"""
        if source_name not in self.data_sources:
            return []
        return self.data_sources[source_name].primary_columns


# Global data manager instance
data_manager = DataManager(os.path.join(os.path.dirname(__file__), "..", "data"))
