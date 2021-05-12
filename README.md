# SelectR Data Manipulation

This Python project will read and parse data in the SelectR format.

## About SelectR

The Standard Electronic Client Transaction Reporting System (SelectR) data format is a structure for various dealers in securities across Canada to provide information on individuals and trades to securities regulator authorities and regulation services providers.

The SE1 data consists of all accounts (client and proprietary) which traded in a particular stock or security within a requested date range. Currently, Staff request and receive the SE1 data from three commercial data service providers, who in turn, maintain it for the back office operations of their respective dealer member customers. The requests for SE1 data are facilitated through a dedicated encrypted portal. All requests must contain the specific security identifier (namely the stock symbol and CUSIP) and the date range.
The SE1 data records the particulars of accounts which bought and sold the particular security as well as the trade terms, the date, the volume and the price. It also contains certain account particulars such as account number, full name and contact information (such as phone number and address) for the account holder, alternate delivery and mailing addresses, if applicable, the dealer member branch at which the account is held and the registered representative’s name and code.


## Installation

Execute the following terminal command in the same directory that the .whl file is stored in:

`pip install OSC_SelectR-{version_number}-py3-none-any.whl`

Replace {version_number} with the actual version number of the file you have.

E.g.

`pip install OSC_SelectR-0.1.1-py3-none-any.whl`

## Usage

You may instantiate a `SelectR` object with the Python command:

```
from selectr import SelectR
foo = SelectR()
```

4 methods are exposed when instantiated without the `folder` argument:

1. get_files(folder)

	Description: This method consumes a string argument "folder" that represents the path to the folder containing the .SE1 files to be processed.
		     If no .SE1 files are found in the folder, an assertion is triggered indicating to the user that no .SE1 files were found. If at least 1 .SE1 file was found in the folder, this method returns a list of the .SE1 file(s) in the folder.
		     NOTE: If a folder is instantiated in the object initialization, the user can call self.files instead of self.get_files(folder).

2. parse(file)

	Description: This method consumes a string argument "file" that represents the name of the .SE1 to be parsed.
		     This method returns a list of dictionaries organized by the section of the data which is one of: "BASIC-CLIENT", "SECURITY-IDENTIFICATION" and "TRADE". 

3. combine(list_)

	Description: This method consumes a list argument "list_" that represents a list of dictionaries. "list_" is expected to be the same ouput from the self.parse(file) function.
		     This method returns a list of three dataframes, one for each of the following sections: "BASIC-CLIENT", "SECURITY-IDENTIFICATION" and "TRADE". 

4. to_df(SE1_files, num_of_processes)

	Description: This method consumes a list argument "SE1_files" that represents a list of strings which are the names of the .SE1 files that are to be processed and cleaned. It also consumes a natural number "num_of_processes" that represents the number of parallel processes the user would like to execute. NOTE: The number of process used should not exceed the number of CPUs your machine has.
		     This method returns a list of three dataframes, one for each of the following sections: "BASIC-CLIENT", "SECURITY-IDENTIFICATION" and "TRADE". 
		     NOTE: If a folder is instantiated in the object initialization, the user can call self.df instead of self.to_df(self.get_files(folder)).

Alternatively, you may also instantiate a `SelectR` object with a `folder` argument:

```
bar = SelectR("./path/to/.se1_files")
```

Doing so will expose 3 additional data objects:

1. folder - confirms the folder
2. files - a list of detected .SE1 files
3. df - a list of parsed data frames from the .SE1 files

