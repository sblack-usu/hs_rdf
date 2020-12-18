from datetime import datetime

from pydantic import AnyUrl, Field, HttpUrl, BaseModel, PositiveInt, validator, root_validator
from rdflib import BNode
from rdflib.term import Identifier as RDFIdentifier

from hs_rdf.namespaces import RDF, RDFS, HSTERMS, DCTERMS
from hs_rdf.schemas.enums import CoverageType, DateType, VariableType, SpatialReferenceType, \
    MultidimensionalSpatialReferenceType, RelationType
from hs_rdf.schemas.root_validators import parse_relation, parse_relation_rdf
from hs_rdf.schemas.validators import validate_user_url


class RDFBaseModel(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class DCTypeInRDF(RDFBaseModel):
    is_defined_by: AnyUrl = Field(rdf_predicate=RDFS.isDefinedBy)
    label: str = Field(rdf_predicate=RDFS.label)


class SourceInRDF(RDFBaseModel):
    is_derived_from: str = Field(rdf_predicate=HSTERMS.isDerivedFrom, default=None)


class Relation(BaseModel):
    type: RelationType
    value: str

    _parse_relation = root_validator(pre=True)(parse_relation)


class RelationInRDF(RDFBaseModel):
    isHostedBy: str = Field(rdf_predicate=HSTERMS.isHostedBy, default=None)
    isCopiedFrom: str = Field(rdf_predicate=HSTERMS.isCopiedFrom, default=None)
    isPartOf: str = Field(rdf_predicate=HSTERMS.isPartOf, default=None)
    hasPart: str = Field(rdf_predicate=HSTERMS.hasPart, default=None)
    isExecutedBy: str = Field(rdf_predicate=HSTERMS.isExecutedBy, default=None)
    isCreatedBy: str = Field(rdf_predicate=HSTERMS.isCreatedBy, default=None)
    isVersionOf: str = Field(rdf_predicate=HSTERMS.isVersionOf, default=None)
    isReplacedBy: str = Field(rdf_predicate=HSTERMS.isReplacedBy, default=None)
    isDataFor: str = Field(rdf_predicate=HSTERMS.isDataFor, default=None)
    cites: str = Field(rdf_predicate=HSTERMS.cites, default=None)
    isDescribedBy: str = Field(rdf_predicate=HSTERMS.isDescribedBy, default=None)

    _parse_relation = root_validator(pre=True)(parse_relation_rdf)


class DescriptionInRDF(RDFBaseModel):
    abstract: str = Field(rdf_predicate=DCTERMS.abstract, default=None)


class IdentifierInRDF(RDFBaseModel):
    hydroshare_identifier: AnyUrl = Field(rdf_predicate=HSTERMS.hydroShareIdentifier)


class ExtendedMetadataInRDF(RDFBaseModel):
    value: str = Field(rdf_predicate=HSTERMS.value)
    key: str = Field(rdf_predicate=HSTERMS.key)


class CellInformation(BaseModel):
    name: str = Field()
    rows: int = Field()
    columns: int = Field()
    cell_size_x_value: float = Field()
    cell_data_type: str = Field()
    cell_size_y_value: float = Field()


class CellInformationInRDF(CellInformation, RDFBaseModel):

    class Config:
        fields = {'name': {"rdf_predicate": HSTERMS.name},
                  'rows': {"rdf_predicate": HSTERMS.rows},
                  'columns': {"rdf_predicate": HSTERMS.columns},
                  'cell_size_x_value': {"rdf_predicate": HSTERMS.cellSizeXValue},
                  'cell_data_type': {"rdf_predicate": HSTERMS.cellDataType},
                  'cell_size_y_value': {"rdf_predicate": HSTERMS.cellSizeYValue}}


class DateInRDF(RDFBaseModel):
    type: DateType = Field(rdf_predicate=RDF.type)
    value: datetime = Field(rdf_predicate=RDF.value)


class Rights(BaseModel):
    rights_statement: str = Field()
    url: AnyUrl = Field()


class RightsInRDF(Rights, RDFBaseModel):

    class Config:
        fields = {'rights_statement': {"rdf_predicate": HSTERMS.rightsStatement},
                  'url': {"rdf_predicate": HSTERMS.URL}}


class Creator(BaseModel):
    name: str = Field(description="The name of a creator", default=None)

    creator_order: PositiveInt = Field(description="the order the creator will appear")
    google_scholar_id: AnyUrl = Field(default=None)
    research_gate_id: AnyUrl = Field(default=None)
    phone: str = Field(default=None)
    ORCID: AnyUrl = Field(default=None)
    address: str = Field(default=None)
    organization: str = Field(default=None)
    email: str = Field(default=None)
    homepage: HttpUrl = Field(default=None)
    description: str = Field(max_length=50, default=None)

    _description_validator = validator("description", pre=True)(validate_user_url)


class CreatorInRDF(Creator, RDFBaseModel):

    class Config:
        fields = {'name': {"rdf_predicate": HSTERMS.name},
                  'creator_order': {"rdf_predicate": HSTERMS.creatorOrder},
                  'google_scholar_id': {"rdf_predicate": HSTERMS.GoogleScholarID},
                  'research_gate_id': {"rdf_predicate": HSTERMS.ResearchGateID},
                  'phone': {"rdf_predicate": HSTERMS.phone},
                  'ORCID': {"rdf_predicate": HSTERMS.ORCID},
                  'address': {"rdf_predicate": HSTERMS.address},
                  'organization': {"rdf_predicate": HSTERMS.organization},
                  'email': {"rdf_predicate": HSTERMS.email},
                  'homepage': {"rdf_predicate": HSTERMS.homepage},
                  'description': {"rdf_predicate": HSTERMS.description}}


class Contributor(BaseModel):
    name: str = Field(default=None)
    google_scholar_id: AnyUrl = Field(default=None)
    research_gate_id: AnyUrl = Field(default=None)
    phone: str = Field(default=None)
    ORCID: AnyUrl = Field(default=None)
    address: str = Field(default=None)
    organization: str = Field(default=None)
    email: str = Field(default=None)
    homepage: HttpUrl = Field(default=None)


class ContributorInRDF(Contributor, RDFBaseModel):

    class Config:
        fields = {'name': {"rdf_predicate": HSTERMS.name},
                  'google_scholar_id': {"rdf_predicate": HSTERMS.GoogleScholarID},
                  'research_gate_id': {"rdf_predicate": HSTERMS.ResearchGateID},
                  'phone': {"rdf_predicate": HSTERMS.phone},
                  'ORCID': {"rdf_predicate": HSTERMS.ORCID},
                  'address': {"rdf_predicate": HSTERMS.address},
                  'organization': {"rdf_predicate": HSTERMS.organization},
                  'email': {"rdf_predicate": HSTERMS.email},
                  'homepage': {"rdf_predicate": HSTERMS.homepage}}


class AwardInfo(BaseModel):
    funding_agency_name: str = Field(default=None)
    award_title: str = Field(default=None)
    award_number: str = Field(default=None)
    funding_agency_url: HttpUrl = Field(default=None)


class AwardInfoInRDF(AwardInfo, RDFBaseModel):

    class Config:
        fields = {'funding_agency_name': {"rdf_predicate": HSTERMS.fundingAgencyName},
                  'award_title': {"rdf_predicate": HSTERMS.awardTitle},
                  'award_number': {"rdf_predicate": HSTERMS.awardNumber},
                  'funding_agency_url': {"rdf_predicate": HSTERMS.fundingAgencyURL}}


class BandInformation(BaseModel):
    name: str = Field()
    variable_name: str = Field(default=None)
    variable_unit: str = Field(default=None)

    no_data_value: str = Field(default=None)
    maximum_value: str = Field(default=None)
    comment: str = Field(default=None)
    method: str = Field(default=None)
    minimum_value: str = Field(default=None)


class BandInformationInRDF(BandInformation, RDFBaseModel):

    class Config:
        fields = {'name': {"rdf_predicate": HSTERMS.name},
                  'variable_name': {"rdf_predicate": HSTERMS.variableName},
                  'variable_unit': {"rdf_predicate": HSTERMS.variableUnit},
                  'no_data_value': {"rdf_predicate": HSTERMS.noDataValue},
                  'maximum_value': {"rdf_predicate": HSTERMS.maximumValue},
                  'comment': {"rdf_predicate": HSTERMS.comment},
                  'method': {"rdf_predicate": HSTERMS.method},
                  'minimum_value': {"rdf_predicate": HSTERMS.minimumValue}}


class CoverageInRDF(RDFBaseModel):
    type: CoverageType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class SpatialReferenceInRDF(RDFBaseModel):
    type: SpatialReferenceType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class MultidimensionalSpatialReferenceInRDF(RDFBaseModel):
    type: MultidimensionalSpatialReferenceType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class FieldInformation(BaseModel):
    field_name: str = Field(default=None)
    field_type: str = Field(default=None)
    field_type_code: str = Field(default=None)
    field_width: int = Field(default=None)
    field_precision: int = Field(default=None)


class FieldInformationInRDF(FieldInformation, RDFBaseModel):

    class Config:
        fields = {'field_name': {"rdf_predicate": HSTERMS.fieldName},
                  'field_type': {"rdf_predicate": HSTERMS.fieldType},
                  'field_type_code': {"rdf_predicate": HSTERMS.fieldTypeCode},
                  'field_width': {"rdf_predicate": HSTERMS.fieldWidth},
                  'field_precision': {"rdf_predicate": HSTERMS.fieldPrecision}}


class GeometryInformation(BaseModel):
    feature_count: int = Field(default=None)
    geometry_type: str = Field(default=None)


class GeometryInformationInRDF(GeometryInformation, RDFBaseModel):

    class Config:
        fields = {'feature_count': {"rdf_predicate": HSTERMS.featureCount},
                  'geometry_type': {"rdf_predicate": HSTERMS.geometryType}}


class Variable(BaseModel):
    name: str = Field()
    unit: str = Field()
    type: VariableType = Field()
    shape: str = Field()
    descriptive_name: str = Field(default=None)
    method: str = Field(default=None)
    missing_value: str = Field(default=None)


class VariableInRDF(Variable, RDFBaseModel):

    class Config:
        fields = {'name': {"rdf_predicate": HSTERMS.name},
                  'unit': {"rdf_predicate": HSTERMS.unit},
                  'type': {"rdf_predicate": HSTERMS.type},
                  'shape': {"rdf_predicate": HSTERMS.shape},
                  'descriptive_name': {"rdf_predicate": HSTERMS.descriptive_name},
                  'method': {"rdf_predicate": HSTERMS.method},
                  'missing_value': {"rdf_predicate": HSTERMS.missing_value}}


class Publisher(BaseModel):
    name: str = Field()
    url: AnyUrl = Field()


class PublisherInRDF(Publisher, RDFBaseModel):

    class Config:
        fields = {'name': {"rdf_predicate": HSTERMS.publisherName},
                  'url': {"rdf_predicate": HSTERMS.publisherURL}}


class TimeSeriesVariable(BaseModel):
    variable_code: str = Field()
    variable_name: str = Field()
    variable_type: str = Field()
    no_data_value: int = Field()
    variable_definition: str = Field(default=None)
    speciation: str = Field(default=None)


class TimeSeriesVariableInRDF(TimeSeriesVariable, RDFBaseModel):

    class Config:
        fields = {'variable_code': {"rdf_predicate": HSTERMS.VariableCode},
                  'variable_name': {"rdf_predicate": HSTERMS.VariableName},
                  'variable_type': {"rdf_predicate": HSTERMS.VariableType},
                  'no_data_value': {"rdf_predicate": HSTERMS.NoDataValue},
                  'variable_definition': {"rdf_predicate": HSTERMS.VariableDefinition},
                  'speciation': {"rdf_predicate": HSTERMS.Speciation}}


class TimeSeriesSite(BaseModel):
    site_code: str = Field()
    site_name: str = Field(default=None)
    elevation_m: float = Field(default=None)
    elevation_datum: str = Field(default=None)
    site_type: str = Field(default=None)
    latitude: float = Field(default=None)
    longitude: float = Field(default=None)


class TimeSeriesSiteInRDF(TimeSeriesSite, RDFBaseModel):

    class Config:
        fields = {'site_code': {"rdf_predicate": HSTERMS.SiteCode},
                  'site_name': {"rdf_predicate": HSTERMS.SiteName},
                  'elevation_m': {"rdf_predicate": HSTERMS.Elevation_m},
                  'elevation_datum': {"rdf_predicate": HSTERMS.ElevationDatum},
                  'site_type': {"rdf_predicate": HSTERMS.SiteType},
                  'latitude': {"rdf_predicate": HSTERMS.Latitude},
                  'longitude': {"rdf_predicate": HSTERMS.Longitude}}


class TimeSeriesMethod(BaseModel):
    method_code: str = Field()
    method_name: str = Field()
    method_type: str = Field()
    method_description: str = Field(default=None)
    method_link: AnyUrl = Field(default=None)


class TimeSeriesMethodInRDF(TimeSeriesMethod, RDFBaseModel):

    class Config:
        fields = {'method_code': {"rdf_predicate": HSTERMS.MethodCode},
                  'method_name': {"rdf_predicate": HSTERMS.MethodName},
                  'method_type': {"rdf_predicate": HSTERMS.MethodType},
                  'method_description': {"rdf_predicate": HSTERMS.MethodDescription},
                  'method_link': {"rdf_predicate": HSTERMS.MethodLink}}


class ProcessingLevel(BaseModel):
    processing_level_code: str = Field()
    definition: str = Field(default=None)
    explanation: str = Field(default=None)


class ProcessingLevelInRDF(ProcessingLevel, RDFBaseModel):

    class Config:
        fields = {'processing_level_code': {"rdf_predicate": HSTERMS.ProcessingLevelCode},
                  'definition': {"rdf_predicate": HSTERMS.Definition},
                  'explanation': {"rdf_predicate": HSTERMS.Explanation}}


class Unit(BaseModel):
    type: str = Field()
    name: str = Field()
    abbreviation: str = Field()


class UnitInRDF(Unit, RDFBaseModel):

    class Config:
        fields = {'type': {"rdf_predicate": HSTERMS.UnitsType},
                  'name': {"rdf_predicate": HSTERMS.UnitsName},
                  'abbreviation': {"rdf_predicate": HSTERMS.UnitsAbbreviation}}


class UTCOffSet(BaseModel):
    value: str = Field(rdf_predicate=HSTERMS.value)


class UTCOffSetInRDF(UTCOffSet, RDFBaseModel):

    class Config:
        fields = {'value': {"rdf_predicate": HSTERMS.value}}


class TimeSeriesResult(BaseModel):
    series_id: str = Field()
    unit: Unit = Field(default=None)
    status: str = Field(default=None)
    sample_medium: str = Field()
    value_count: int = Field()
    aggregation_statistics: str = Field()
    series_label: str = Field(default=None)
    site: TimeSeriesSite = Field()
    variable: TimeSeriesVariable = Field()
    method: TimeSeriesMethod = Field()
    processing_level: ProcessingLevel = Field()
    utc_offset: UTCOffSet = Field(default=None)


class TimeSeriesResultInRDF(TimeSeriesResult, RDFBaseModel):

    unit: UnitInRDF = Field(rdf_predicate=HSTERMS.unit, default=None)
    site: TimeSeriesSiteInRDF = Field(rdf_predicate=HSTERMS.site)
    variable: TimeSeriesVariableInRDF = Field(rdf_predicate=HSTERMS.variable)
    method: TimeSeriesMethodInRDF = Field(rdf_predicate=HSTERMS.method)
    processing_level: ProcessingLevelInRDF = Field(rdf_predicate=HSTERMS.processingLevel)
    utc_offset: UTCOffSetInRDF = Field(rdf_predicate=HSTERMS.UTCOffSet, default=None)

    class Config:
        fields = {'series_id': {"rdf_predicate": HSTERMS.timeSeriesResultUUID},
                  'status': {"rdf_predicate": HSTERMS.Status},
                  'sample_medium': {"rdf_predicate": HSTERMS.SampleMedium},
                  'value_count': {"rdf_predicate": HSTERMS.ValueCount},
                  'aggregation_statistics': {"rdf_predicate": HSTERMS.AggregationStatistic},
                  'series_label': {"rdf_predicate": HSTERMS.SeriesLabel}}
