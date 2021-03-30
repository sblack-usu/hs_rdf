# hsclient
A python client for interacting with HydroShare in an object oriented way.

## Jupyter Notebooks
HydroShare has a resource with example notebooks.  Click [here](https://www.hydroshare.org/resource/7561aa12fd824ebb8edbee05af19b910/) then click the blue `Open with...` dropdown and select `Cuahsi Jupyterhub` to launch the notebooks into a Jupyter Environment to start using this project.


## Install the HS RDF HydroShare Python Client
The HS RDF Python Client for HydroShare won't be installed by default, so it has to be installed first before you can work with it. Use the following command to install the Python Client from the GitHub repository. Eventually we will distribute this package via the Python Package Index (PyPi) so that it can be installed via pip from PyPi.

```bash
pip install hsclient
```

## Authenticate with HydroShare
Before you start interacting with resources in HydroShare you will need to authenticate.
```python
from hsclient import HydroShare

hs = HydroShare()
hs.sign_in()
```

## Create a New Empty Resource
A "resource" is a container for your content in HydroShare. Think of it as a "working directory" into which you are going to organize the code and/or data you are using and want to share. The following code can be used to create a new, empty resource within which you can create content and metadata.

This code creates a new resource in HydroShare. It also creates an in-memory object representation of that resource in your local environmment that you can then manipulate with further code.
```python
# Create the new, empty resource
new_resource = hs.create()

# Get the HydroShare identifier for the new resource
resIdentifier = new_resource.resource_id
print('The HydroShare Identifier for your new resource is: ' + resIdentifier)

# Construct a hyperlink for the new resource
print('Your new resource is available at: ' +  new_resource.metadata.url)
```

# Creating and Editing Resource Metadata Elements
Editing metadata elements for a resource can be done in an object oriented way. You can specify all of the metadata elements in code, which will set their values in memory in your local environment. Values of metadata elements can be edited, removed, or replaced by setting them to a new value, appending new values (in the case where the metadata element accepts a list), or by removing the value entirely.

When you are ready to save edits to metadata elements from your local environment to the resource in HydroShare, you can call the save() function on your resource and all of the new metadata values you created/edited will be saved to the resource in HydroShare.

## Resource Title and Abstract
The Title and Abstract metadata elements can be specified as text strings. To modify the Title or Abstract after it has been set, just set them to a different value.

```python
# Set the Title for the resource
new_resource.metadata.title = 'Resource for Testing the HS RDF HydroShare Python Client'

# Set the Abstract text for the resource
new_resource.metadata.abstract = (
    'This resource was created as a demonstration of using the HS RDF ' 
    'Python Client for HydroShare. Once you have completed all of the '
    'steps in this notebook, you will have a fully populated HydroShare '
    'Resource.'
)

# Call the save function to save the metadata edits to HydroShare
new_resource.save()

# Print the title just added to the resource
print('Title: ' + new_resource.metadata.title)
print('Abstract: ' + new_resource.metadata.abstract)
```
