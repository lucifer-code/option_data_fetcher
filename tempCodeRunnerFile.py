if 'data' in data:
    # Convert data to DataFrame
    df = pd.DataFrame(data['data'])

    # Save data to JSON file
    df.to_json('data.json', orient='records', indent=4)

    # Save data to Excel file
    df.to_excel('data.xlsx', index=False)
    
    print("Data saved as data.json and data.xlsx in the current directory.")
else:
    print("No data available.")

