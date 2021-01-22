# hsclient
A python client for interacting with HydroShare in an object oriented way.

## Jupyter Notebooks
HydroShare has a resource with example notebooks.  Click [here](https://www.hydroshare.org/resource/7561aa12fd824ebb8edbee05af19b910/) then click the blue `Open with...` dropdown and select `Cuahsi Jupyterhub` to launch the notebooks into a Jupyter Environment to start using this project.

## Example:

```python
from hsclient import HydroShare

# username/password can be passed to Hydroshare constructor
hs = HydroShare()
# or you can call sign_in() for prompts
hs.sign_in()

# retrieves a resource by id
resource = hs.resource('09041bbe8015485db414a4d41b3575db')

# access metadata object and title attribute
print(resource.metadata.title)

from pathlib import Path

# loop through files not associated with an aggregation
for f in resource.files:
    Path("temp/" + f.folder).mkdir(parents=True, exist_ok=True)
    # download each file to temp and the relative path within the resource
    f.download("temp/" + f.path)

# loop through aggregations in the resource
for agg in resource.aggregations:
    # access metadata object and title attribute of aggregation
    print(agg.metadata.title)
    # loop through files in the aggregation
    for f in agg.files:
        Path("temp/" + f.folder).mkdir(parents=True, exist_ok=True)
        # download each file to temp and the relative path within the aggregation
        f.download("temp/" + f.path)
```

