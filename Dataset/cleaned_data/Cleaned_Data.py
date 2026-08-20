import pandas as pd
import numpy as np


# ============================================================
# STEP 1 - LOAD DATASET
# ============================================================

df = pd.read_csv(
    r"C:\Users\Admin\Desktop\MetricMind-AI\Dataset\raw_data\Sales_Records_Dataset_dirty.csv"
)

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())


# ============================================================
# STEP 2 - CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ============================================================
# STEP 3 - CHECK DUPLICATE ROWS
# ============================================================

print("\nDuplicate Rows:", df.duplicated().sum())


# ============================================================
# STEP 4 - REMOVE DUPLICATE ROWS
# ============================================================

df.drop_duplicates(inplace=True)

print("Shape After Removing Duplicates:", df.shape)


# ============================================================
# STEP 5 - HANDLE MISSING COUNTRY VALUES
# ============================================================

df["Country"] = df["Country"].fillna(
    df["Country"].mode()[0]
)

print(
    "Missing Country Values:",
    df["Country"].isnull().sum()
)


# ============================================================
# STEP 6 - HANDLE MISSING ORDER PRIORITY
# ============================================================

df["Order Priority"] = df["Order Priority"].fillna(
    df["Order Priority"].mode()[0]
)

print(
    "Missing Order Priority Values:",
    df["Order Priority"].isnull().sum()
)


# ============================================================
# STEP 7 - HANDLE MISSING UNIT PRICE
# ============================================================

df["Unit Price"] = df["Unit Price"].fillna(
    df["Unit Price"].median()
)

print(
    "Missing Unit Price Values:",
    df["Unit Price"].isnull().sum()
)


# ============================================================
# STEP 8 - CHECK ORDER DATE
# IMPORTANT:
# DO NOT FILL MISSING ORDER DATES WITH MODE
# ============================================================

print("\n========== ORDER DATE BEFORE CONVERSION ==========")

print(
    "Missing Order Date:",
    df["Order Date"].isnull().sum()
)

print(
    df["Order Date"].head(10)
)


# ============================================================
# STEP 9 - CONVERT ORDER DATE AND SHIP DATE
# ============================================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed",
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="mixed",
    errors="coerce"
)


print("\n========== DATE CONVERSION CHECK ==========")

print("Order Date type:", df["Order Date"].dtype)
print("Ship Date type:", df["Ship Date"].dtype)

print(
    "Invalid Order Dates:",
    df["Order Date"].isna().sum()
)

print(
    "Invalid Ship Dates:",
    df["Ship Date"].isna().sum()
)


# ============================================================
# STEP 10 - CHECK ORDER DATE VS SHIP DATE
# ============================================================

invalid_shipping = df[
    df["Ship Date"] < df["Order Date"]
]

print("\n========== SHIPPING DATE VALIDATION ==========")

print(
    "Ship Date before Order Date:",
    len(invalid_shipping)
)

if len(invalid_shipping) > 0:

    print("\nProblematic Rows:")

    print(
        invalid_shipping[
            ["Order ID", "Order Date", "Ship Date"]
        ].to_string(index=False)
    )


# ============================================================
# STEP 11 - CHECK MISSING ORDER DATES
# ============================================================

print("\n========== FINAL DATE CHECK ==========")

print(
    "Missing Order Dates:",
    df["Order Date"].isna().sum()
)

print(
    "Missing Ship Dates:",
    df["Ship Date"].isna().sum()
)

print("\nFirst 10 Order Dates:")

print(
    df["Order Date"].head(10)
)

print("\nFirst 10 Ship Dates:")

print(
    df["Ship Date"].head(10)
)

# ============================================================
# STEP 12 - FINAL MISSING VALUE CHECK
# ============================================================

print("\n========== STEP 12: MISSING VALUE CHECK ==========")

missing_values = df.isnull().sum()

print(missing_values)

print("\nTotal Missing Values:", missing_values.sum())

print("\nColumns With Missing Values:")

print(
    missing_values[missing_values > 0]
)

# ============================================================
# STEP 12A - INVESTIGATE MISSING ORDER DATES
# ============================================================

missing_order_dates = df[
    df["Order Date"].isna()
]

print("\n========== STEP 12A: MISSING ORDER DATE DETAILS ==========")

print(
    "Rows with missing Order Date:",
    len(missing_order_dates)
)

print("\nSample of missing Order Date records:")

print(
    missing_order_dates[
        ["Order ID", "Order Date", "Ship Date"]
    ].head(20).to_string(index=False)
)

print("\nShip Date range for missing Order Dates:")

print(
    "Minimum Ship Date:",
    missing_order_dates["Ship Date"].min()
)

print(
    "Maximum Ship Date:",
    missing_order_dates["Ship Date"].max()
)



# Step 12B — Check duplicate Order IDs among these records
print("\nDuplicate Order IDs among missing Order Dates:")

print(
    missing_order_dates["Order ID"].duplicated().sum()
)


# ============================================================
# STEP 12C - HANDLE MISSING ORDER DATES
# ============================================================

# We will NOT replace missing Order Dates with mode,
# median, or Ship Date because that would create false data.

print("\n========== STEP 12C: ORDER DATE DECISION ==========")

print(
    "Missing Order Dates kept as missing:",
    df["Order Date"].isna().sum()
)

print(
    "Missing Order Dates are represented as NaT:",
    df["Order Date"].isna().sum()
)



# ============================================================
# STEP 13 - DUPLICATE CHECK
# ============================================================

print("\n========== STEP 13: DUPLICATE CHECK ==========")

duplicate_rows = df.duplicated().sum()

print("Duplicate Rows:", duplicate_rows)

print("\nCurrent Dataset Shape:", df.shape)

# ============================================================
# STEP 14 - DATA TYPE VALIDATION
# ============================================================

print("\n========== STEP 14: DATA TYPE VALIDATION ==========")

print("\nData Types:")
print(df.dtypes)

print("\nData Type Summary:")
print(df.info())


# ============================================================
# STEP 15 - NUMERICAL VALUE VALIDATION
# ============================================================

print("\n========== STEP 15: NUMERICAL VALUE VALIDATION ==========")

numeric_columns = [
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit"
]

print("\n========== DESCRIPTIVE STATISTICS ==========")

print(
    df[numeric_columns].describe()
)


# ------------------------------------------------------------
# CHECK NEGATIVE VALUES
# ------------------------------------------------------------

print("\n========== NEGATIVE VALUE CHECK ==========")

for column in numeric_columns:
    negative_count = (df[column] < 0).sum()
    print(f"{column}: {negative_count} negative values")


# ------------------------------------------------------------
# CHECK ZERO VALUES
# ------------------------------------------------------------

print("\n========== ZERO VALUE CHECK ==========")

for column in numeric_columns:
    zero_count = (df[column] == 0).sum()
    print(f"{column}: {zero_count} zero values")


# ------------------------------------------------------------
# CHECK NULL VALUES
# ------------------------------------------------------------

print("\n========== NUMERIC NULL CHECK ==========")

print(
    df[numeric_columns].isnull().sum()
)


# ============================================================
# STEP 15A - INVESTIGATE NEGATIVE UNITS SOLD
# ============================================================

negative_units = df[df["Units Sold"] < 0]

print("\n========== STEP 15A: NEGATIVE UNITS SOLD ==========")

print("Negative Units Sold rows:", len(negative_units))

print("\nSample negative Units Sold records:")

print(
    negative_units[
        [
            "Order ID",
            "Order Date",
            "Ship Date",
            "Units Sold",
            "Unit Price",
            "Unit Cost",
            "Total Revenue",
            "Total Cost",
            "Total Profit"
        ]
    ].head(20).to_string(index=False)
)


# ============================================================
# STEP 15B - INVESTIGATE ZERO UNIT PRICE
# ============================================================

zero_price = df[df["Unit Price"] == 0]

print("\n========== STEP 15B: ZERO UNIT PRICE ==========")

print("Zero Unit Price rows:", len(zero_price))

print("\nSample zero Unit Price records:")

print(
    zero_price[
        [
            "Order ID",
            "Order Date",
            "Ship Date",
            "Units Sold",
            "Unit Price",
            "Unit Cost",
            "Total Revenue",
            "Total Cost",
            "Total Profit"
        ]
    ].head(20).to_string(index=False)
)


# ============================================================
# STEP 15C - CHECK NUMERICAL CONSISTENCY
# ============================================================

print("\n========== STEP 15C: NUMERICAL CONSISTENCY ==========")

# Check Revenue calculation
df["Calculated Revenue"] = (
    df["Units Sold"].abs() * df["Unit Price"]
)

revenue_difference = (
    df["Total Revenue"] - df["Calculated Revenue"]
).abs()

print(
    "Rows where Total Revenue does not match "
    "Units Sold × Unit Price:",
    (revenue_difference > 0.01).sum()
)


# Check Cost calculation
df["Calculated Cost"] = (
    df["Units Sold"].abs() * df["Unit Cost"]
)

cost_difference = (
    df["Total Cost"] - df["Calculated Cost"]
).abs()

print(
    "Rows where Total Cost does not match "
    "Units Sold × Unit Cost:",
    (cost_difference > 0.01).sum()
)


# Show negative Units Sold calculation
print("\nSample negative Units Sold consistency:")

print(
    df[df["Units Sold"] < 0][
        [
            "Units Sold",
            "Unit Price",
            "Total Revenue",
            "Calculated Revenue"
        ]
    ].head(10).to_string(index=False)
)


# Show zero Unit Price consistency
print("\nSample zero Unit Price consistency:")

print(
    df[df["Unit Price"] == 0][
        [
            "Units Sold",
            "Unit Price",
            "Total Revenue",
            "Calculated Revenue"
        ]
    ].head(10).to_string(index=False)
)


# Remove temporary columns after checking
df.drop(
    columns=["Calculated Revenue", "Calculated Cost"],
    inplace=True
)

# ============================================================
# STEP 15D - CORRECT NUMERICAL DATA ERRORS
# ============================================================

print("\n========== STEP 15D: CORRECT NUMERICAL ERRORS ==========")

# ------------------------------------------------------------
# 1. Correct negative Units Sold
# ------------------------------------------------------------

negative_before = (df["Units Sold"] < 0).sum()

print(
    "Negative Units Sold before correction:",
    negative_before
)

df["Units Sold"] = df["Units Sold"].abs()

negative_after = (df["Units Sold"] < 0).sum()

print(
    "Negative Units Sold after correction:",
    negative_after
)


# ------------------------------------------------------------
# 2. Identify zero Unit Price records
# ------------------------------------------------------------

zero_price_before = (df["Unit Price"] == 0).sum()

print(
    "\nZero Unit Price before correction:",
    zero_price_before
)


# ------------------------------------------------------------
# 3. Recover zero Unit Price using Revenue / Units Sold
# ------------------------------------------------------------

zero_price_mask = (
    (df["Unit Price"] == 0) &
    (df["Units Sold"] > 0)
)

df.loc[zero_price_mask, "Unit Price"] = (
    df.loc[zero_price_mask, "Total Revenue"]
    / df.loc[zero_price_mask, "Units Sold"]
)


# ------------------------------------------------------------
# 4. Check zero Unit Price after correction
# ------------------------------------------------------------

zero_price_after = (df["Unit Price"] == 0).sum()

print(
    "Zero Unit Price after correction:",
    zero_price_after
)


# ------------------------------------------------------------
# 5. Display corrected records
# ------------------------------------------------------------

print("\nSample corrected Unit Price records:")

print(
    df[
        df["Order ID"].isin(
            zero_price_mask[zero_price_mask].index
        )
    ][
        [
            "Order ID",
            "Units Sold",
            "Unit Price",
            "Total Revenue"
        ]
    ].head(20).to_string(index=False)
)


# ------------------------------------------------------------
# 6. Final check
# ------------------------------------------------------------

print("\n========== NUMERICAL CORRECTION SUMMARY ==========")

print(
    "Negative Units Sold remaining:",
    (df["Units Sold"] < 0).sum()
)

print(
    "Zero Unit Price remaining:",
    (df["Unit Price"] == 0).sum()
)

# ============================================================
# STEP 15E - POST-CORRECTION NUMERICAL VALIDATION
# ============================================================

print("\n========== STEP 15E: POST-CORRECTION VALIDATION ==========")

numeric_columns = [
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit"
]

# Check negative values
print("\nNegative Values:")

for column in numeric_columns:
    count = (df[column] < 0).sum()
    print(f"{column}: {count}")


# Check zero values
print("\nZero Values:")

for column in numeric_columns:
    count = (df[column] == 0).sum()
    print(f"{column}: {count}")


# Check missing numeric values
print("\nMissing Numeric Values:")

print(
    df[numeric_columns].isnull().sum()
)


# Check basic statistics
print("\nUpdated Numerical Statistics:")

print(
    df[numeric_columns].describe()
)

# ============================================================
# STEP 16 - CATEGORICAL VALUE VALIDATION
# ============================================================

print("\n========== STEP 16: CATEGORICAL VALUE VALIDATION ==========")

categorical_columns = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Priority"
]

for column in categorical_columns:

    print("\n----------------------------------------")
    print("COLUMN:", column)
    print("Unique Values:", df[column].nunique())
    print("----------------------------------------")

    print(df[column].value_counts(dropna=False))

# ============================================================
# STEP 16A - CHECK CATEGORICAL WHITESPACE
# ============================================================

print("\n========== STEP 16A: CATEGORICAL WHITESPACE CHECK ==========")

for column in categorical_columns:

    leading_spaces = (
        df[column].astype(str).str.startswith(" ")
    ).sum()

    trailing_spaces = (
        df[column].astype(str).str.endswith(" ")
    ).sum()

    print(
        f"{column}: "
        f"Leading spaces = {leading_spaces}, "
        f"Trailing spaces = {trailing_spaces}"
    ) 

# ============================================================
# STEP 16B - CLEAN CATEGORICAL WHITESPACE
# ============================================================

print("\n========== STEP 16B: CLEAN CATEGORICAL WHITESPACE ==========")

categorical_columns = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Priority"
]

# Count unique values before cleaning
print("Unique Country values BEFORE cleaning:",
      df["Country"].nunique())

# Remove leading and trailing spaces
for column in categorical_columns:
    df[column] = df[column].str.strip()

# Count unique values after cleaning
print("Unique Country values AFTER cleaning:",
      df["Country"].nunique())


# Check whitespace again
print("\n========== WHITESPACE CHECK AFTER CLEANING ==========")

for column in categorical_columns:

    leading_spaces = (
        df[column].astype(str).str.startswith(" ")
    ).sum()

    trailing_spaces = (
        df[column].astype(str).str.endswith(" ")
    ).sum()

    print(
        f"{column}: "
        f"Leading spaces = {leading_spaces}, "
        f"Trailing spaces = {trailing_spaces}"
    )

# ============================================================
# STEP 16C - VERIFY COUNTRY VALUES
# ============================================================

print("\n========== STEP 16C: COUNTRY VERIFICATION ==========")

print("Unique Countries:", df["Country"].nunique())

print("\nTop 20 Countries:")

print(
    df["Country"].value_counts().head(20)
)

# ============================================================
# STEP 17 - FINAL DATE VALIDATION
# ============================================================

print("\n========== STEP 17: FINAL DATE VALIDATION ==========")

# ------------------------------------------------------------
# 1. Check date data types
# ------------------------------------------------------------

print("\nDate Data Types:")

print("Order Date:", df["Order Date"].dtype)
print("Ship Date :", df["Ship Date"].dtype)


# ------------------------------------------------------------
# 2. Check missing dates
# ------------------------------------------------------------

print("\nMissing Date Values:")

print(
    df[["Order Date", "Ship Date"]].isnull().sum()
)


# ------------------------------------------------------------
# 3. Check invalid date order
# ------------------------------------------------------------

invalid_shipping = df[
    df["Order Date"].notna() &
    df["Ship Date"].notna() &
    (df["Ship Date"] < df["Order Date"])
]

print(
    "\nShip Date before Order Date:",
    len(invalid_shipping)
)


# ------------------------------------------------------------
# 4. Display problematic rows if any
# ------------------------------------------------------------

if len(invalid_shipping) > 0:

    print("\nProblematic Date Records:")

    print(
        invalid_shipping[
            [
                "Order ID",
                "Order Date",
                "Ship Date"
            ]
        ]
        .head(20)
        .to_string(index=False)
    )

else:

    print(
        "\nNo records found where Ship Date "
        "is before Order Date."
    )


# ------------------------------------------------------------
# 5. Date range
# ------------------------------------------------------------

print("\nDate Range:")

print(
    "Minimum Order Date:",
    df["Order Date"].min()
)

print(
    "Maximum Order Date:",
    df["Order Date"].max()
)

print(
    "Minimum Ship Date:",
    df["Ship Date"].min()
)

print(
    "Maximum Ship Date:",
    df["Ship Date"].max()
)

# ============================================================
# STEP 18 - BUSINESS RULE VALIDATION
# ============================================================

print("\n========== STEP 18: BUSINESS RULE VALIDATION ==========")


# ------------------------------------------------------------
# 1. Calculate expected Total Revenue
# ------------------------------------------------------------

df["Expected Revenue"] = (
    df["Units Sold"] * df["Unit Price"]
)

revenue_difference = (
    df["Total Revenue"] - df["Expected Revenue"]
).abs()

print(
    "\nRevenue calculation mismatches:",
    (revenue_difference > 0.01).sum()
)


# ------------------------------------------------------------
# 2. Calculate expected Total Cost
# ------------------------------------------------------------

df["Expected Cost"] = (
    df["Units Sold"] * df["Unit Cost"]
)

cost_difference = (
    df["Total Cost"] - df["Expected Cost"]
).abs()

print(
    "Cost calculation mismatches:",
    (cost_difference > 0.01).sum()
)


# ------------------------------------------------------------
# 3. Calculate expected Total Profit
# ------------------------------------------------------------

df["Expected Profit"] = (
    df["Total Revenue"] - df["Total Cost"]
)

profit_difference = (
    df["Total Profit"] - df["Expected Profit"]
).abs()

print(
    "Profit calculation mismatches:",
    (profit_difference > 0.01).sum()
)


# ------------------------------------------------------------
# 4. Show sample mismatches
# ------------------------------------------------------------

revenue_errors = df[
    revenue_difference > 0.01
]

if len(revenue_errors) > 0:

    print("\nSample Revenue Mismatches:")

    print(
        revenue_errors[
            [
                "Units Sold",
                "Unit Price",
                "Total Revenue",
                "Expected Revenue"
            ]
        ]
        .head(10)
        .to_string(index=False)
    )


profit_errors = df[
    profit_difference > 0.01
]

if len(profit_errors) > 0:

    print("\nSample Profit Mismatches:")

    print(
        profit_errors[
            [
                "Total Revenue",
                "Total Cost",
                "Total Profit",
                "Expected Profit"
            ]
        ]
        .head(10)
        .to_string(index=False)
    )


# ------------------------------------------------------------
# 5. Remove temporary validation columns
# ------------------------------------------------------------

df.drop(
    columns=[
        "Expected Revenue",
        "Expected Cost",
        "Expected Profit"
    ],
    inplace=True
)


print("\nTemporary validation columns removed.")

print("\nCurrent Dataset Shape:", df.shape)

# ============================================================
# STEP 18A - INVESTIGATE REVENUE MISMATCHES
# ============================================================

print("\n========== STEP 18A: REVENUE MISMATCH INVESTIGATION ==========")

# Calculate expected revenue again
expected_revenue = (
    df["Units Sold"] * df["Unit Price"]
)

revenue_difference = (
    df["Total Revenue"] - expected_revenue
).abs()

revenue_errors = df[
    revenue_difference > 0.01
].copy()

print(
    "Revenue mismatch rows:",
    len(revenue_errors)
)


# ------------------------------------------------------------
# Check which Unit Prices are involved
# ------------------------------------------------------------

print("\nUnit Prices in Revenue Mismatches:")

print(
    revenue_errors["Unit Price"]
    .value_counts()
    .head(20)
)


# ------------------------------------------------------------
# Check Item Types
# ------------------------------------------------------------

print("\nItem Types in Revenue Mismatches:")

print(
    revenue_errors["Item Type"]
    .value_counts()
)


# ------------------------------------------------------------
# Check Sales Channels
# ------------------------------------------------------------

print("\nSales Channels in Revenue Mismatches:")

print(
    revenue_errors["Sales Channel"]
    .value_counts()
)


# ------------------------------------------------------------
# Show sample records
# ------------------------------------------------------------

print("\nSample Revenue Mismatch Records:")

print(
    revenue_errors[
        [
            "Order ID",
            "Item Type",
            "Sales Channel",
            "Units Sold",
            "Unit Price",
            "Unit Cost",
            "Total Revenue",
            "Total Cost",
            "Total Profit"
        ]
    ]
    .head(30)
    .to_string(index=False)
)

# ============================================================
# STEP 18B - RECOVER CORRECT UNIT PRICE
# ============================================================

print("\n========== STEP 18B: RECOVER CORRECT UNIT PRICE ==========")

# Identify the corrupted Unit Price
revenue_error_mask = (
    (df["Unit Price"] == 154.06) &
    (
        (df["Total Revenue"] -
         (df["Units Sold"] * df["Unit Price"])).abs()
        > 0.01
    )
)

print(
    "Rows with corrupted Unit Price:",
    revenue_error_mask.sum()
)


# Calculate the likely correct Unit Price
df["Recovered Unit Price"] = (
    df["Total Revenue"] / df["Units Sold"]
)


# Show recovered prices
print("\nRecovered Unit Price values:")

print(
    df.loc[
        revenue_error_mask,
        "Recovered Unit Price"
    ]
    .round(2)
    .value_counts()
    .sort_index()
)


# Show sample
print("\nSample recovered prices:")

print(
    df.loc[
        revenue_error_mask,
        [
            "Order ID",
            "Units Sold",
            "Unit Price",
            "Total Revenue",
            "Recovered Unit Price"
        ]
    ]
    .head(20)
    .to_string(index=False)
)

# ============================================================
# STEP 18C - CORRECT CORRUPTED UNIT PRICE
# ============================================================

print("\n========== STEP 18C: CORRECT CORRUPTED UNIT PRICE ==========")

# Count corrupted prices before correction
corrupted_before = (
    (df["Unit Price"] == 154.06) &
    (
        (df["Total Revenue"] -
         (df["Units Sold"] * df["Unit Price"])).abs()
        > 0.01
    )
).sum()

print(
    "Corrupted Unit Price rows before correction:",
    corrupted_before
)


# Replace corrupted Unit Price with recovered price
df.loc[
    revenue_error_mask,
    "Unit Price"
] = df.loc[
    revenue_error_mask,
    "Recovered Unit Price"
]


# Remove temporary column
df.drop(
    columns=["Recovered Unit Price"],
    inplace=True
)


# Count remaining revenue mismatches
expected_revenue_after = (
    df["Units Sold"] * df["Unit Price"]
)

revenue_difference_after = (
    df["Total Revenue"] - expected_revenue_after
).abs()

remaining_revenue_errors = (
    revenue_difference_after > 0.01
).sum()


print(
    "Revenue mismatches after correction:",
    remaining_revenue_errors
)


print(
    "Current Dataset Shape:",
    df.shape
)

# ============================================================
# STEP 18D - FINAL BUSINESS RULE VALIDATION
# ============================================================

print("\n========== STEP 18D: FINAL BUSINESS RULE VALIDATION ==========")


# Revenue
expected_revenue = (
    df["Units Sold"] * df["Unit Price"]
)

revenue_errors = (
    df["Total Revenue"] - expected_revenue
).abs()

print(
    "Revenue mismatches:",
    (revenue_errors > 0.01).sum()
)


# Cost
expected_cost = (
    df["Units Sold"] * df["Unit Cost"]
)

cost_errors = (
    df["Total Cost"] - expected_cost
).abs()

print(
    "Cost mismatches:",
    (cost_errors > 0.01).sum()
)


# Profit
expected_profit = (
    df["Total Revenue"] - df["Total Cost"]
)

profit_errors = (
    df["Total Profit"] - expected_profit
).abs()

print(
    "Profit mismatches:",
    (profit_errors > 0.01).sum()
)

# ============================================================
# STEP 19 - ORDER ID VALIDATION
# ============================================================

print("\n========== STEP 19: ORDER ID VALIDATION ==========")

# 1. Missing Order IDs
print("\nMissing Order IDs:")
print(df["Order ID"].isnull().sum())


# 2. Duplicate Order IDs
print("\nDuplicate Order IDs:")
print(df["Order ID"].duplicated().sum())


# 3. Unique Order IDs
print("\nUnique Order IDs:")
print(df["Order ID"].nunique())


# 4. Order ID data type
print("\nOrder ID Data Type:")
print(df["Order ID"].dtype)


# 5. Minimum and maximum Order ID
print("\nOrder ID Range:")
print("Minimum:", df["Order ID"].min())
print("Maximum:", df["Order ID"].max())


# 6. Check invalid/non-positive IDs
print("\nNon-positive Order IDs:")
print((df["Order ID"] <= 0).sum())


# 7. Display duplicate Order IDs if any
duplicate_order_ids = df[
    df["Order ID"].duplicated(keep=False)
]

print("\nDuplicate Order ID Records:")

if len(duplicate_order_ids) > 0:
    print(
        duplicate_order_ids[
            ["Order ID", "Order Date", "Ship Date"]
        ]
        .sort_values("Order ID")
        .head(20)
        .to_string(index=False)
    )
else:
    print("No duplicate Order IDs found.")


# ============================================================
# STEP 20 - DUPLICATE ORDER ID INVESTIGATION
# ============================================================

print("\n========== STEP 20: DUPLICATE ORDER ID INVESTIGATION ==========")

# Get all rows having duplicate Order IDs
duplicate_ids = df[
    df["Order ID"].duplicated(keep=False)
].copy()

print(
    "Rows with duplicate Order IDs:",
    len(duplicate_ids)
)

print(
    "Number of duplicated Order IDs:",
    duplicate_ids["Order ID"].nunique()
)


# ------------------------------------------------------------
# Check whether duplicate rows are completely identical
# ------------------------------------------------------------

duplicate_all_columns = duplicate_ids.duplicated(
    keep=False
)

print(
    "\nRows that are completely identical:",
    duplicate_all_columns.sum()
)


# ------------------------------------------------------------
# Check duplicate Order IDs with different information
# ------------------------------------------------------------

duplicate_different = duplicate_ids[
    ~duplicate_ids.duplicated(
        keep=False
    )
]

print(
    "Rows that are not completely identical:",
    len(duplicate_different)
)


# ------------------------------------------------------------
# Show all duplicate Order IDs
# ------------------------------------------------------------

print("\nDuplicate Order IDs and counts:")

print(
    duplicate_ids["Order ID"]
    .value_counts()
    .to_string()
)


# ------------------------------------------------------------
# STEP 22: Show duplicate records that have different information
# ------------------------------------------------------------

print(
    "\n========== DUPLICATES WITH DIFFERENT INFORMATION =========="
)

if len(duplicate_different) > 0:

    print(
        duplicate_different[
            [
                "Order ID",
                "Region",
                "Country",
                "Item Type",
                "Sales Channel",
                "Order Priority",
                "Order Date",
                "Ship Date",
                "Units Sold",
                "Unit Price",
                "Unit Cost",
                "Total Revenue",
                "Total Cost",
                "Total Profit"
            ]
        ]
        .sort_values("Order ID")
        .to_string(index=False)
    )

else:

    print(
        "All duplicate Order ID rows are completely identical."
    )

df = df.drop_duplicates(subset=["Order ID"])



print("\n========== STEP 21: DUPLICATE REMOVAL VALIDATION ==========")

print("Current Dataset Shape:", df.shape)

print("Duplicate Order IDs:", df["Order ID"].duplicated().sum())

print("Unique Order IDs:", df["Order ID"].nunique())

print("\nMissing Order Dates:")
print(df["Order Date"].isna().sum())

print("\nMissing Ship Dates:")
print(df["Ship Date"].isna().sum())

# ============================================================
# STEP 22: MISSING ORDER DATE INVESTIGATION 
# ============================================================

print("\n========== STEP 22: MISSING ORDER DATE INVESTIGATION ==========")

missing_order_dates = df[df["Order Date"].isna()].copy()

print("Rows with Missing Order Date:", len(missing_order_dates))

print("\nSample Missing Order Date Records:")
print(
    missing_order_dates[
        ["Order ID", "Ship Date", "Region", "Country",
         "Item Type", "Sales Channel", "Units Sold",
         "Unit Price", "Total Revenue"]
    ].head(20).to_string(index=False)
)

print("\nMissing Order Date by Region:")
print(missing_order_dates["Region"].value_counts())

print("\nMissing Order Date by Country:")
print(missing_order_dates["Country"].value_counts().head(20))

# ============================================================
# STEP 23: ORDER DATE RECOVERY ANALYSIS
# ============================================================

print("\n========== STEP 23: ORDER DATE RECOVERY ANALYSIS ==========")

missing_dates = df[df["Order Date"].isna()].copy()

# Calculate the available date range of valid records
valid_dates = df["Order Date"].dropna()

print("Valid Order Date Minimum:", valid_dates.min())
print("Valid Order Date Maximum:", valid_dates.max())

print("\nMissing Order Date Rows:", len(missing_dates))

# Check whether Ship Date falls within the normal date range
print("\nShip Dates for Missing Order Dates:")
print("Minimum Ship Date:", missing_dates["Ship Date"].min())
print("Maximum Ship Date:", missing_dates["Ship Date"].max())

# Check common shipping delays in the complete records
complete = df[df["Order Date"].notna()].copy()

complete["Shipping Days"] = (
    complete["Ship Date"] - complete["Order Date"]
).dt.days

print("\nShipping Days Statistics:")
print(complete["Shipping Days"].describe())

print("\nMost Common Shipping Delays:")
print(complete["Shipping Days"].value_counts().head(20))

# ============================================================
# STEP 24: FINAL MISSING DATE VALIDATION
# ============================================================

print("\n========== STEP 24: FINAL MISSING DATE VALIDATION ==========")

# Missing Order Date records
missing_dates = df[df["Order Date"].isna()].copy()

print("Missing Order Dates:", len(missing_dates))

# Check whether any missing Order Date has Ship Date missing
missing_both_dates = df[
    df["Order Date"].isna() & df["Ship Date"].isna()
]

print("Missing Both Order Date and Ship Date:",
      len(missing_both_dates))

# Check whether all missing Order Dates have valid Ship Dates
print("\nMissing Order Date with Valid Ship Date:",
      df["Order Date"].isna().sum() -
      missing_both_dates.shape[0])

# Check numerical/business-rule consistency again
revenue_expected = df["Units Sold"] * df["Unit Price"]
cost_expected = df["Units Sold"] * df["Unit Cost"]
profit_expected = df["Total Revenue"] - df["Total Cost"]

revenue_mismatch = (
    (df["Total Revenue"] - revenue_expected).abs() > 0.01
).sum()

cost_mismatch = (
    (df["Total Cost"] - cost_expected).abs() > 0.01
).sum()

profit_mismatch = (
    (df["Total Profit"] - profit_expected).abs() > 0.01
).sum()

print("\nBusiness Rule Validation:")
print("Revenue mismatches:", revenue_mismatch)
print("Cost mismatches:", cost_mismatch)
print("Profit mismatches:", profit_mismatch)

# Date relationship check
date_issue = (
    df["Order Date"].notna() &
    df["Ship Date"].notna() &
    (df["Ship Date"] < df["Order Date"])
).sum()

print("\nShip Date before Order Date:", date_issue)

# Numeric validation
numeric_columns = [
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit"
]

print("\nNegative Numeric Values:")
for col in numeric_columns:
    print(f"{col}: {(df[col] < 0).sum()}")

print("\nMissing Numeric Values:")
print(df[numeric_columns].isna().sum())

# ============================================================
# STEP 25: FINAL DATASET QUALITY CHECK 
# ============================================================

print("\n========== STEP 25: FINAL DATASET QUALITY CHECK ==========")

# 1. Dataset shape
print("\nDataset Shape:")
print(df.shape)

# 2. Column names
print("\nColumns:")
print(df.columns.tolist())

# 3. Duplicate complete rows
print("\nCompletely Duplicate Rows:")
print(df.duplicated().sum())

# 4. Duplicate Order IDs
print("\nDuplicate Order IDs:")
print(df["Order ID"].duplicated().sum())

# 5. Unique Order IDs
print("\nUnique Order IDs:")
print(df["Order ID"].nunique())

# 6. Missing values
print("\nMissing Values by Column:")
print(df.isna().sum())

# 7. Negative values
numeric_columns = [
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit"
]

print("\nNegative Values:")
for col in numeric_columns:
    print(f"{col}: {(df[col] < 0).sum()}")

# 8. Zero values
print("\nZero Values:")
for col in numeric_columns:
    print(f"{col}: {(df[col] == 0).sum()}")

# 9. Data types
print("\nData Types:")
print(df.dtypes)

# 10. Categorical unique values
categorical_columns = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Priority"
]

print("\nCategorical Unique Values:")
for col in categorical_columns:
    print(f"{col}: {df[col].nunique()}")

# 11. Date range
print("\nDate Range:")
print("Order Date Minimum:", df["Order Date"].min())
print("Order Date Maximum:", df["Order Date"].max())
print("Ship Date Minimum:", df["Ship Date"].min())
print("Ship Date Maximum:", df["Ship Date"].max())

# 12. Business rule validation
revenue_expected = df["Units Sold"] * df["Unit Price"]
cost_expected = df["Units Sold"] * df["Unit Cost"]
profit_expected = df["Total Revenue"] - df["Total Cost"]

print("\nBusiness Rule Validation:")

print(
    "Revenue mismatches:",
    ((df["Total Revenue"] - revenue_expected).abs() > 0.01).sum()
)

print(
    "Cost mismatches:",
    ((df["Total Cost"] - cost_expected).abs() > 0.01).sum()
)

print(
    "Profit mismatches:",
    ((df["Total Profit"] - profit_expected).abs() > 0.01).sum()
)

# 13. Date relationship
date_errors = (
    df["Order Date"].notna() &
    df["Ship Date"].notna() &
    (df["Ship Date"] < df["Order Date"])
).sum()

print("\nShip Date Before Order Date:")
print(date_errors)

print("\n========== STEP 25 COMPLETE ==========")


# ============================================================
# STEP 26: REMOVE ROWS WITH MISSING ORDER DATE
# ============================================================

print("\n========== STEP 26: REMOVE MISSING ORDER DATE ROWS ==========")

# Count missing Order Date rows before removal
missing_order_dates_before = df["Order Date"].isna().sum()

print(f"Missing Order Date rows before removal: {missing_order_dates_before}")

# Remove rows where Order Date is missing
df = df.dropna(subset=["Order Date"]).copy()

# Count missing Order Date rows after removal
missing_order_dates_after = df["Order Date"].isna().sum()

print(f"Missing Order Date rows after removal: {missing_order_dates_after}")

# Show updated dataset shape
print(f"Dataset Shape after removing missing Order Dates: {df.shape}")

print("\n========== STEP 26 COMPLETE ==========")

# ============================================================
# STEP 27: FINAL DATASET VALIDATION
# ============================================================

print("\n========== STEP 27: FINAL DATASET VALIDATION ==========")

# ------------------------------------------------------------
# 1. DATASET SHAPE
# ------------------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

# ------------------------------------------------------------
# 2. COLUMN VALIDATION
# ------------------------------------------------------------

print("\nColumns:")
print(df.columns.tolist())

print(f"\nNumber of Columns: {len(df.columns)}")
print(f"Number of Rows: {len(df)}")

# ------------------------------------------------------------
# 3. COMPLETE DUPLICATE ROWS
# ------------------------------------------------------------

duplicate_rows = df.duplicated().sum()

print("\nCompletely Duplicate Rows:")
print(duplicate_rows)

# ------------------------------------------------------------
# 4. ORDER ID VALIDATION
# ------------------------------------------------------------

duplicate_order_ids = df["Order ID"].duplicated().sum()
unique_order_ids = df["Order ID"].nunique()

print("\nDuplicate Order IDs:")
print(duplicate_order_ids)

print("\nUnique Order IDs:")
print(unique_order_ids)

# ------------------------------------------------------------
# 5. MISSING VALUES
# ------------------------------------------------------------

print("\nMissing Values by Column:")
print(df.isna().sum())

total_missing = df.isna().sum().sum()

print(f"\nTotal Missing Values: {total_missing}")

# ------------------------------------------------------------
# 6. NEGATIVE VALUES
# ------------------------------------------------------------

numeric_columns = [
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit"
]

print("\nNegative Values:")

for col in numeric_columns:
    negative_count = (df[col] < 0).sum()
    print(f"{col}: {negative_count}")

# ------------------------------------------------------------
# 7. ZERO VALUES
# ------------------------------------------------------------

print("\nZero Values:")

for col in numeric_columns:
    zero_count = (df[col] == 0).sum()
    print(f"{col}: {zero_count}")

# ------------------------------------------------------------
# 8. DATA TYPES
# ------------------------------------------------------------

print("\nData Types:")
print(df.dtypes)

# ------------------------------------------------------------
# 9. CATEGORICAL UNIQUE VALUES
# ------------------------------------------------------------

categorical_columns = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Priority"
]

print("\nCategorical Unique Values:")

for col in categorical_columns:
    print(f"{col}: {df[col].nunique()}")

# ------------------------------------------------------------
# 10. DATE VALIDATION
# ------------------------------------------------------------

print("\nDate Range:")

print("Order Date Minimum:", df["Order Date"].min())
print("Order Date Maximum:", df["Order Date"].max())

print("Ship Date Minimum:", df["Ship Date"].min())
print("Ship Date Maximum:", df["Ship Date"].max())

# Missing dates
missing_order_dates = df["Order Date"].isna().sum()
missing_ship_dates = df["Ship Date"].isna().sum()

print("\nMissing Order Dates:")
print(missing_order_dates)

print("Missing Ship Dates:")
print(missing_ship_dates)

# Ship date before order date
invalid_dates = (df["Ship Date"] < df["Order Date"]).sum()

print("\nShip Date Before Order Date:")
print(invalid_dates)

# ------------------------------------------------------------
# 11. BUSINESS RULE VALIDATION
# ------------------------------------------------------------

calculated_revenue = (
    df["Units Sold"] * df["Unit Price"]
).round(2)

calculated_cost = (
    df["Units Sold"] * df["Unit Cost"]
).round(2)

calculated_profit = (
    df["Total Revenue"] - df["Total Cost"]
).round(2)

revenue_mismatches = (
    df["Total Revenue"].round(2) != calculated_revenue
).sum()

cost_mismatches = (
    df["Total Cost"].round(2) != calculated_cost
).sum()

profit_mismatches = (
    df["Total Profit"].round(2) != calculated_profit
).sum()

print("\nBusiness Rule Validation:")

print("Revenue mismatches:", revenue_mismatches)
print("Cost mismatches:", cost_mismatches)
print("Profit mismatches:", profit_mismatches)

# ------------------------------------------------------------
# 12. FINAL DATA QUALITY SUMMARY
# ------------------------------------------------------------

print("\n========== FINAL DATA QUALITY SUMMARY ==========")

if (
    duplicate_rows == 0
    and duplicate_order_ids == 0
    and total_missing == 0
    and revenue_mismatches == 0
    and cost_mismatches == 0
    and profit_mismatches == 0
    and invalid_dates == 0
):

    print("STATUS: DATASET PASSED FINAL VALIDATION")
    print("All major data quality checks passed.")

else:

    print("STATUS: DATASET REQUIRES FURTHER REVIEW")

print("\n========== STEP 27 COMPLETE ==========")


# ============================================================
# STEP 27A: CREATE INSIGHT COLUMNS
# ============================================================

print("\n========== STEP 27A: CREATE INSIGHT COLUMNS ==========")

# Shipping Days
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# Profit Margin %
df["Profit Margin %"] = (
    df["Total Profit"] / df["Total Revenue"]
) * 100

# Order Year
df["Order Year"] = df["Order Date"].dt.year

# Month Name
df["Month Name"] = df["Order Date"].dt.month_name()

# Year-Month
df["Year-Month"] = df["Order Date"].dt.strftime("%Y-%m")

# Order Month Number
df["Order Month"] = df["Order Date"].dt.month

# Order Quarter
df["Order Quarter"] = df["Order Date"].dt.quarter

print("New columns added successfully.")

print("\nCurrent Dataset Shape:")
print(df.shape)

print("\nNew Columns:")
print([
    "Shipping Days",
    "Profit Margin %",
    "Order Year",
    "Month Name",
    "Year-Month",
    "Order Month",
    "Order Quarter"
])

print("\n========== STEP 27A COMPLETE ==========")


# ============================================================
# STEP 28: SAVE FINAL CLEANED DATASET
# ============================================================

print("\n========== STEP 28: SAVE FINAL DATASET ==========")

final_file = "MetricMind_Final_Cleaned_Dataset.csv"

# Save dataset
df.to_csv(final_file, index=False)

print(f"Final dataset saved successfully: {final_file}")
print(f"Final dataset shape: {df.shape}")

# ============================================================
# VERIFY SAVED CSV
# ============================================================

check_df = pd.read_csv(final_file)

print("\n========== SAVED CSV VERIFICATION ==========")

print("Saved Dataset Shape:", check_df.shape)

print("\nSaved Dataset Columns:")
print(check_df.columns.tolist())

print("\nNumber of Columns:", len(check_df.columns))
print("Number of Rows:", len(check_df))

print("\n========== STEP 28 COMPLETE ==========")

print("\n========== FINAL DATASET CHECK ==========")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Rows:")
print(df.head())

print("\n========== FINAL CHECK COMPLETE ==========")