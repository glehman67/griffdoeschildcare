import streamlit as st

# Tuition data as a list of dicts
DATA = [
    # Full-Time Infant
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $40K", "Tuition": 77},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $100K", "Tuition": 275},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $120K", "Tuition": 275},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $40K", "Tuition": 77},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $120K", "Tuition": 275},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $40K", "Tuition": 69},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $120K", "Tuition": 231},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $40K", "Tuition": 62},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $120K", "Tuition": 231},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $40K", "Tuition": 46},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $60K", "Tuition": 104},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $120K", "Tuition": 231},
    # Full-Time Toddler
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $40K", "Tuition": 77},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $100K", "Tuition": 250},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $120K", "Tuition": 250},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $40K", "Tuition": 77},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $120K", "Tuition": 250},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $40K", "Tuition": 69},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $120K", "Tuition": 231},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $40K", "Tuition": 62},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $120K", "Tuition": 231},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $40K", "Tuition": 46},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $60K", "Tuition": 104},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $120K", "Tuition": 231},
    # Full-Time Pre-School
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $40K", "Tuition": 77},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $100K", "Tuition": 244},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $120K", "Tuition": 244},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $40K", "Tuition": 77},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $120K", "Tuition": 244},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $40K", "Tuition": 69},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $120K", "Tuition": 231},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $40K", "Tuition": 62},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $60K", "Tuition": 115},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $120K", "Tuition": 231},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $40K", "Tuition": 46},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $60K", "Tuition": 104},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $80K", "Tuition": 154},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $100K", "Tuition": 192},
    {"Care Type": "Full-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $120K", "Tuition": 231},
    # Part-Time Infant
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $40K", "Tuition": 39},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $100K", "Tuition": 138},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 2, "Income Level": "Approximately $120K", "Tuition": 138},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $40K", "Tuition": 39},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 3, "Income Level": "Approximately $120K", "Tuition": 138},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $40K", "Tuition": 35},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 4, "Income Level": "Approximately $120K", "Tuition": 138},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $40K", "Tuition": 35},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 5, "Income Level": "Approximately $120K", "Tuition": 116},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $40K", "Tuition": 23},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $60K", "Tuition": 52},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Infant - 6 Weeks to 12 months", "Household Size": 6, "Income Level": "Approximately $120K", "Tuition": 116},
    # Part-Time Toddler
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $40K", "Tuition": 39},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $100K", "Tuition": 125},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 2, "Income Level": "Approximately $120K", "Tuition": 125},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $40K", "Tuition": 39},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 3, "Income Level": "Approximately $120K", "Tuition": 125},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $40K", "Tuition": 35},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 4, "Income Level": "Approximately $120K", "Tuition": 116},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $40K", "Tuition": 31},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 5, "Income Level": "Approximately $120K", "Tuition": 116},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $40K", "Tuition": 23},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $60K", "Tuition": 52},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Toddler - 13 - 36 Months", "Household Size": 6, "Income Level": "Approximately $120K", "Tuition": 116},
    # Part-Time Pre-School
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $40K", "Tuition": 39},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $100K", "Tuition": 122},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 2, "Income Level": "Approximately $120K", "Tuition": 122},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $40K", "Tuition": 39},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 3, "Income Level": "Approximately $120K", "Tuition": 122},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $40K", "Tuition": 35},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 4, "Income Level": "Approximately $120K", "Tuition": 116},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $40K", "Tuition": 31},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $60K", "Tuition": 58},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 5, "Income Level": "Approximately $120K", "Tuition": 116},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $40K", "Tuition": 23},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $60K", "Tuition": 52},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $80K", "Tuition": 77},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $100K", "Tuition": 96},
    {"Care Type": "Part-Time", "Age Group": "Pre-School - Over 36 Months", "Household Size": 6, "Income Level": "Approximately $120K", "Tuition": 116},
]

def get_tuition(care_type, age_group, household_size, income_level):
    for row in DATA:
        if (
            row["Care Type"] == care_type and
            row["Age Group"] == age_group and
            row["Household Size"] == household_size and
            row["Income Level"] == income_level
        ):
            return row["Tuition"]
    return None

st.title("Weekly Tuition Calculator")

care_type = st.selectbox("Care Type", ["Full-Time", "Part-Time"])
age_group = st.selectbox("Age Group", [
    "Infant - 6 Weeks to 12 months",
    "Toddler - 13 - 36 Months",
    "Pre-School - Over 36 Months"
])
household_size = st.selectbox("Household Size", [2, 3, 4, 5, 6])
income_level = st.selectbox("Income Level", [
    "Approximately $40K",
    "Approximately $60K",
    "Approximately $80K",
    "Approximately $100K",
    "Approximately $120K"
])

if st.button("Calculate Tuition"):
    tuition = get_tuition(care_type, age_group, household_size, income_level)
    if tuition is not None:
        st.success(f"Approximate Weekly Tuition: ${tuition}")
    else:
        st.error("No tuition data found for the selected options.")
