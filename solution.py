"""
Simple Loyalty Assessment - Table Output & Processing
Candidate: [Your Name]
Position: Internship - Software Engineer MY
Date: January 2026

This script processes data from Table 1 (stored in SQLite database) 
and calculates Table 2 values as per assessment requirements.
"""

import sqlite3
import os


class TableProcessor:
    """Handles database operations and table processing"""
    
    def __init__(self, db_name='assessment.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Establish database connection"""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print(f"✓ Connected to database: {self.db_name}")
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            print("✓ Database connection closed")
    
    def initialize_database(self):
        """Create and populate tables from SQL file"""
        print("\n--- Initializing Database ---")
        
        # Read and execute SQL file
        with open('database.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        
        self.cursor.executescript(sql_script)
        self.conn.commit()
        print("✓ Database initialized with Table 1 data")
    
    def display_table_1(self):
        """Retrieve and display all data from Table 1"""
        print("\n" + "="*50)
        print("TABLE 1: SOURCE DATA")
        print("="*50)
        print(f"{'Cell':<10} {'Value':<10}")
        print("-"*50)
        
        self.cursor.execute("SELECT cell_name, value FROM table_1 ORDER BY cell_name")
        rows = self.cursor.fetchall()
        
        table_1_data = {}
        for cell_name, value in rows:
            print(f"{cell_name:<10} {value:<10}")
            table_1_data[cell_name] = value
        
        print("="*50)
        return table_1_data
    
    def calculate_table_2(self, table_1_data):
        """
        Calculate Table 2 values based on Table 1 data
        
        Requirements:
        - Alpha: A5 + A20
        - Beta: A15 / A7
        - Charlie: A13 * A12
        """
        calculations = {
            'Alpha': {
                'formula': 'A5 + A20',
                'value': table_1_data['A5'] + table_1_data['A20']
            },
            'Beta': {
                'formula': 'A15 / A7',
                'value': table_1_data['A15'] / table_1_data['A7']
            },
            'Charlie': {
                'formula': 'A13 * A12',
                'value': table_1_data['A13'] * table_1_data['A12']
            }
        }
        
        return calculations
    
    def save_table_2(self, calculations):
        """Save calculated results to Table 2 in database"""
        # Clear existing data
        self.cursor.execute("DELETE FROM table_2")
        
        # Insert calculated values
        for category, data in calculations.items():
            self.cursor.execute(
                "INSERT INTO table_2 (category, formula, value) VALUES (?, ?, ?)",
                (category, data['formula'], data['value'])
            )
        
        self.conn.commit()
        print("✓ Table 2 results saved to database")
    
    def display_table_2(self):
        """Retrieve and display Table 2 from database"""
        print("\n" + "="*50)
        print("TABLE 2: CALCULATED RESULTS")
        print("="*50)
        print(f"{'Category':<15} {'Formula':<15} {'Value':<15}")
        print("-"*50)
        
        self.cursor.execute("SELECT category, formula, value FROM table_2 ORDER BY category")
        rows = self.cursor.fetchall()
        
        for category, formula, value in rows:
            print(f"{category:<15} {formula:<15} {value:<15.2f}")
        
        print("="*50)
    
    def verify_calculations(self, table_1_data, calculations):
        """Verify that calculations are correct"""
        print("\n--- Verification ---")
        
        # Verify Alpha
        expected_alpha = table_1_data['A5'] + table_1_data['A20']
        actual_alpha = calculations['Alpha']['value']
        print(f"Alpha: {table_1_data['A5']} + {table_1_data['A20']} = {actual_alpha} ✓" if expected_alpha == actual_alpha else "✗")
        
        # Verify Beta
        expected_beta = table_1_data['A15'] / table_1_data['A7']
        actual_beta = calculations['Beta']['value']
        print(f"Beta: {table_1_data['A15']} / {table_1_data['A7']} = {actual_beta:.2f} ✓" if abs(expected_beta - actual_beta) < 0.001 else "✗")
        
        # Verify Charlie
        expected_charlie = table_1_data['A13'] * table_1_data['A12']
        actual_charlie = calculations['Charlie']['value']
        print(f"Charlie: {table_1_data['A13']} * {table_1_data['A12']} = {actual_charlie} ✓" if expected_charlie == actual_charlie else "✗")


def main():
    """Main execution function"""
    print("\n" + "="*50)
    print("SIMPLE LOYALTY - TABLE PROCESSING ASSESSMENT")
    print("="*50)
    
    # Initialize processor
    processor = TableProcessor()
    
    try:
        # Connect to database
        processor.connect()
        
        # Initialize database with data from SQL file
        processor.initialize_database()
        
        # Display Table 1
        table_1_data = processor.display_table_1()
        
        # Calculate Table 2
        print("\n--- Processing Calculations ---")
        calculations = processor.calculate_table_2(table_1_data)
        print("✓ Calculations completed")
        
        # Save to database
        processor.save_table_2(calculations)
        
        # Display Table 2
        processor.display_table_2()
        
        # Verify calculations
        processor.verify_calculations(table_1_data, calculations)
        
        print("\n" + "="*50)
        print("ASSESSMENT COMPLETED SUCCESSFULLY")
        print("="*50)
        print(f"\nDatabase saved as: {processor.db_name}")
        print("All tables and calculations are stored in the database.")
        
    except Exception as e:
        print(f"\n✗ Error occurred: {str(e)}")
        raise
    
    finally:
        # Close database connection
        processor.close()


if __name__ == "__main__":
    main()
