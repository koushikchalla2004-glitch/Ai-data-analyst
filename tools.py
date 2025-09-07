import argparse
import polars as pl
import os

def run_analysis(file_path, question):
    """Performs analysis based on the question."""
    try:
        df = pl.read_csv(file_path)
        print(f"Dataset has {df.height} rows and {df.width} columns.")

        if "average delivery rating" in question.lower():
            average_rating = df['Service Rating'].mean()
            return f"The average delivery service rating is: {average_rating:.2f}"

        elif "total orders" in question.lower():
            total_orders = df.shape[0]
            return f"The total number of orders is: {total_orders}"

        else:
            return "Sorry, I can't answer that question yet."

    except Exception as e:
        return f"An error occurred during analysis: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a sales dataset.")
    parser.add_argument('file_path', type=str, help="The path to the dataset.")
    parser.add_argument('question', type=str, help="The question to analyze the data.")
    args = parser.parse_args()
    
    result = run_analysis(args.file_path, args.question)
    print(result)
