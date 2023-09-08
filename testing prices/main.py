from tools import to_use

### EXCEL STUFF

import pandas as pd
# Read the files
products = pd.read_excel('testing prices\data_export.xlsx', sheet_name='Sheet1')

sold_products = pd.read_excel('testing prices\Cel_mai_bine_vandute_produse.xlsx', sheet_name='Sheet1')

# Merge the DataFrames on the 'SKU' column
merged_data = pd.merge(sold_products, products, on='SKU', how='left')

# Create a DataFrame to store unmatched products
unmatched_products = merged_data[merged_data['prices'].isnull()]

# Remove unmatched products from the main sheet
merged_data = merged_data.dropna(subset=['prices'])

# Replace empty values in the 'Producator' column with 'Other'
merged_data['Producator'].fillna('Other', inplace=True)

# Calculate profits using the get_profit function
merged_data['Profit'] = merged_data['prices'].apply(to_use.get_profit)

main_page = pd.DataFrame()
main_page.to_excel('testing prices\merged_data.xlsx', sheet_name='Main Page', index=False)

# Save the matched data to the main sheet in a new Excel file
# Save the unmatched products to a new sheet in the same Excel file
with pd.ExcelWriter('testing prices\merged_data.xlsx', mode='a', engine='openpyxl') as writer:
    merged_data.to_excel(writer, sheet_name='Matched Products', index=False)
    unmatched_products.to_excel(writer, sheet_name='Unmatched Products', index=False)
    

