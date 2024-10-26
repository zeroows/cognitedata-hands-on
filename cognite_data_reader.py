from datetime import datetime, timedelta
import pandas as pd

# I have created this class to read data from CDF and perform basic statistical analysis on the retrieved data.
class CogniteDataReader:
    """
    A class for reading and processing data from Cognite Data Fusion (CDF).

    This class provides methods to interact with CDF, retrieve time series data,
    and perform basic statistical analysis on the retrieved data.

    Attributes:
        client: A CogniteClient instance for interacting with CDF.
    """

    def __init__(self, client):
        """
        Initialize the CogniteDataReader with a CogniteClient.

        Args:
            client: A CogniteClient instance.
        """
        self.client = client

    def print_stats(self, assets_df):
        """
        Print statistics about the given DataFrame.

        This method calculates and prints basic statistical measures (mean, median, min, max)
        for the given DataFrame.

        Args:
            assets_df (pd.DataFrame): A DataFrame containing numerical data to analyze.

        Returns:
            None

        Prints:
            Asset Statistics including mean, median, min, and max for each column in the DataFrame.
        """
        stats = assets_df.agg(['mean', 'median', 'min', 'max'])
        print("Asset Statistics:")
        for stat, value in stats.items():
            print(f"{stat.capitalize()}: {value}")

    def get_time_series_by_external_id(self, external_id: str, start: str = "5w-ago", end: str = "now"):
        """
        Get time series data associated with a specific external ID.

        This method retrieves time series data from CDF for the given external ID
        within the specified time range. It also prints basic statistics about the
        retrieved data.

        Args:
            external_id (str): The external ID of the time series.
            start (str): A string representing the start time. Default is "5w-ago".
            end (str): A string representing the end time. Default is "now".

        Returns:
            pd.DataFrame: A DataFrame containing the retrieved time series data,
                          or None if no data is found or an error occurs.

        Raises:
            Exception: If there's an error retrieving the time series data.
        """
        try:
            time_series = self.client.time_series.data.retrieve(external_id=external_id, start=start, end=end).to_pandas()
            if time_series.empty:
                print(f"No time series found with external ID: {external_id}")
                return None
            else:
                print("--------------------------------")
                print(f"Time series data for {external_id}:")
                self.print_stats(time_series[external_id])
                print("--------------------------------")
                return time_series
                
        except Exception as e:
            print(f"Error retrieving time series data: {str(e)}")
            return None