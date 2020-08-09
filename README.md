
# Get Association Scores from the Open Targets Platform

Welcome! This is a small application to fetch the association scores for a given target or disease ID.

For any given target or disease ID this package allows you to:

1. Store into a JSON file the target-disease association information resulting from the query.
2. See a simple analysis of the scores indicating the maximum, minimum and average and standard deviation values of the overall association scores of each target or disease.

This package accesses the **Open Targets Platform REST API** data, more precisely from its association endpoint. You can see their [documentation](https://docs.targetvalidation.org/programmatic-access/rest-api) for more information. 

## Installation 

Simply install it via:

```bash
git clone https://github.com/ireneisdoomed/otp_associations.git
```

from the [source on GitHub.](https://github.com/ireneisdoomed/otp_associations.git)

## Requirements

The package only requires the [requests](https://requests.readthedocs.io/en/master/) and [numpy](https://numpy.org/doc/stable/) modules to access and process the data. The program has been tested with the versions indicated in the requirements file on Python version 3.8.3.

## Usage

The command-line program admits two different parameters for analysis:

- -d: The ID of the disease for which you want to do the analysis. *For example: EFO_0000384*
- -t: The ID of the target for which you want to do the analysis. *For example: ENSG00000167207*

It also supports two other optional parameters:

- -e: Exports the result of the query to JSON format. You have to indicate the output filename.
- -m: Minimum score value to filter associations with a certain quality data point. Default is set to 0. Scores above 0.2 is a good trade-off
  
An example of the usage may be:

```bash
python main.py -d EFO_0000384 -m 0.2 -e EFO_0000384.json
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


