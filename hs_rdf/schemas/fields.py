from datetime import datetime

from pydantic import AnyUrl, Field, HttpUrl, BaseModel
from rdflib import BNode
from rdflib.term import Identifier as RDFIdentifier

from hs_rdf.namespaces import RDF, RDFS, HSTERMS, DCTERMS
from hs_rdf.schemas.enums import CoverageType, DateType, VariableType, SpatialReferenceType, \
    MultidimensionalSpatialReferenceType


class DCTypeInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    is_defined_by: AnyUrl = Field(rdf_predicate=RDFS.isDefinedBy)
    label: str = Field(rdf_predicate=RDFS.label)


class SourceInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    is_derived_from: str = Field(rdf_predicate=HSTERMS.isDerivedFrom, default=None)


class Relation(BaseModel):
    is_copied_from: AnyUrl = Field(rdf_predicate=HSTERMS.isCopiedFrom, default=None)
    is_part_of: AnyUrl = Field(rdf_predicate=HSTERMS.isPartOf, default=None)
    is_described_by: AnyUrl = Field(rdf_predicate=HSTERMS.isDescribedBy, default=None)


class RelationInRDF(Relation):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class DescriptionInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    abstract: str = Field(rdf_predicate=DCTERMS.abstract, default=None)


class IdentifierInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    hydroshare_identifier: AnyUrl = Field(rdf_predicate=HSTERMS.hydroShareIdentifier)


class ExtendedMetadataInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    value: str = Field(rdf_predicate=HSTERMS.value)
    key: str = Field(rdf_predicate=HSTERMS.key)


class CellInformation(BaseModel):
    name: str = Field(rdf_predicate=HSTERMS.name)
    rows: int = Field(rdf_predicate=HSTERMS.rows)
    columns: int = Field(rdf_predicate=HSTERMS.columns)
    cell_size_x_value: float = Field(rdf_predicate=HSTERMS.cellSizeXValue)
    cell_data_type: str = Field(rdf_predicate=HSTERMS.cellDataType)
    cell_size_y_value: float = Field(rdf_predicate=HSTERMS.cellSizeYValue)


class CellInformationInRDF(CellInformation):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class DateInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    type: DateType = Field(rdf_predicate=RDF.type)
    value: datetime = Field(rdf_predicate=RDF.value)


class Rights(BaseModel):
    rights_statement: str = Field(rdf_predicate=HSTERMS.rightsStatement)
    url: AnyUrl = Field(rdf_predicate=HSTERMS.URL)


class RightsInRDF(Rights):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class Creator(BaseModel):
    name: str = Field(rdf_predicate=HSTERMS.name, description="The name of a creator", default=None)

    creator_order: int = Field(rdf_predicate=HSTERMS.creatorOrder, description="the order the creator will appear")
    google_scholar_id: AnyUrl = Field(rdf_predicate=HSTERMS.GoogleScholarID, default=None)
    research_gate_id: AnyUrl = Field(rdf_predicate=HSTERMS.ResearchGateID, default=None)
    phone: str = Field(rdf_predicate=HSTERMS.phone, default=None)
    ORCID: AnyUrl = Field(rdf_predicate=HSTERMS.ORCID, default=None)
    address: str = Field(rdf_predicate=HSTERMS.address, default=None)
    organization: str = Field(rdf_predicate=HSTERMS.organization, default=None)
    email: str = Field(rdf_predicate=HSTERMS.email, default=None)
    homepage: HttpUrl = Field(rdf_predicate=HSTERMS.homepage, default=None)
    description: str = Field(rdf_predicate=HSTERMS.description, default=None)


class CreatorInRDF(Creator):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class Contributor(BaseModel):
    name: str = Field(rdf_predicate=HSTERMS.name, default=None)
    google_scholar_id: AnyUrl = Field(rdf_predicate=HSTERMS.GoogleScholarID, default=None)
    research_gate_id: AnyUrl = Field(rdf_predicate=HSTERMS.ResearchGateID, default=None)
    phone: str = Field(rdf_predicate=HSTERMS.phone, default=None)
    ORCID: AnyUrl = Field(rdf_predicate=HSTERMS.ORCID, default=None)
    address: str = Field(rdf_predicate=HSTERMS.address, default=None)
    organization: str = Field(rdf_predicate=HSTERMS.organization, default=None)
    email: str = Field(rdf_predicate=HSTERMS.email, default=None)
    homepage: HttpUrl = Field(rdf_predicate=HSTERMS.homepage, default=None)


class ContributorInRDF(Contributor):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class AwardInfo(BaseModel):
    funding_agency_name: str = Field(rdf_predicate=HSTERMS.fundingAgencyName, default=None)
    award_title: str = Field(rdf_predicate=HSTERMS.awardTitle, default=None)
    award_number: str = Field(rdf_predicate=HSTERMS.awardNumber, default=None)
    funding_agency_url: HttpUrl = Field(rdf_predicate=HSTERMS.fundingAgencyURL, default=None)


class AwardInfoInRDF(AwardInfo):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class BandInformation(BaseModel):
    name: str = Field(rdf_predicate=HSTERMS.name)
    variable_name: str = Field(rdf_predicate=HSTERMS.variableName, default=None)
    variable_unit: str = Field(rdf_predicate=HSTERMS.variableUnit, default=None)

    no_data_value: str = Field(rdf_predicate=HSTERMS.noDataValue, default=None)
    maximum_value: str = Field(rdf_predicate=HSTERMS.maximumValue, default=None)
    comment: str = Field(rdf_predicate=HSTERMS.comment, default=None)
    method: str = Field(rdf_predicate=HSTERMS.method, default=None)
    minimum_value: str = Field(rdf_predicate=HSTERMS.minimumValue, default=None)


class BandInformationInRDF(BandInformation):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class CoverageInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    type: CoverageType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class SpatialReferenceInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    type: SpatialReferenceType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class MultidimensionalSpatialReferenceInRDF(BaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)
    type: MultidimensionalSpatialReferenceType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class FieldInformation(BaseModel):
    fieldname: str = Field(rdf_predicate=HSTERMS.fieldName, default=None)
    fieldtype: str = Field(rdf_predicate=HSTERMS.fieldType, default=None)
    fieldTypeCode: str = Field(rdf_predicate=HSTERMS.fieldTypeCode, default=None)
    fieldWidth: int = Field(rdf_predicate=HSTERMS.fieldWidth, default=None)
    fieldPrecision: int = Field(rdf_predicate=HSTERMS.fieldPrecision, default=None)


class FieldInformationInRDF(FieldInformation):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class GeometryInformation(BaseModel):
    featureCount: int = Field(rdf_predicate=HSTERMS.featureCount, default=None)
    geometryType: str = Field(rdf_predicate=HSTERMS.geometryType, default=None)


class GeometryInformationInRDF(GeometryInformation):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class Variable(BaseModel):
    name: str = Field(rdf_predicate=HSTERMS.name)
    unit: str = Field(rdf_predicate=HSTERMS.unit)
    type: VariableType = Field(rdf_predicate=HSTERMS.type)
    shape: str = Field(rdf_predicate=HSTERMS.shape)
    descriptive_name: str = Field(rdf_predicate=HSTERMS.descriptive_name, default=None)
    method: str = Field(rdf_predicate=HSTERMS.method, default=None)
    missing_value: str = Field(rdf_predicate=HSTERMS.missing_value, default=None)


class VariableInRDF(Variable):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class Publisher(BaseModel):
    name: str = Field(rdf_predicate=HSTERMS.publisherName)
    url: AnyUrl = Field(rdf_predicate=HSTERMS.publisherURL)


class PublisherInRDF(Publisher):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class TimeSeriesVariable(BaseModel):
    variable_code: str = Field(rdf_predicate=HSTERMS.VariableCode)
    variable_name: str = Field(rdf_predicate=HSTERMS.VariableName)
    variable_type: str = Field(rdf_predicate=HSTERMS.VariableType)
    no_data_value: int = Field(rdf_predicate=HSTERMS.NoDataValue)
    variable_definition: str = Field(rdf_predicate=HSTERMS.VariableDefinition, default=None)
    speciation: str = Field(rdf_predicate=HSTERMS.Speciation, default=None)


class TimeSeriesVariableInRDF(TimeSeriesVariable):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class TimeSeriesSite(BaseModel):
    site_code: str = Field(rdf_predicate=HSTERMS.SiteCode)
    site_name: str = Field(rdf_predicate=HSTERMS.SiteName, default=None)
    elevation_m: float = Field(rdf_predicate=HSTERMS.Elevation_m, default=None)
    elevation_datum: str = Field(rdf_predicate=HSTERMS.ElevationDatum, default=None)
    site_type: str = Field(rdf_predicate=HSTERMS.SiteType, default=None)
    latitude: float = Field(rdf_predicate=HSTERMS.Latitude, default=None)
    longitude: float = Field(rdf_predicate=HSTERMS.Longitude, default=None)


class TimeSeriesSiteInRDF(TimeSeriesSite):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class TimeSeriesMethod(BaseModel):
    method_code: str = Field(rdf_predicate=HSTERMS.MethodCode)
    method_name: str = Field(rdf_predicate=HSTERMS.MethodName)
    method_type: str = Field(rdf_predicate=HSTERMS.MethodType)
    method_description: str = Field(rdf_predicate=HSTERMS.MethodDescription, default=None)
    method_link: AnyUrl = Field(rdf_predicate=HSTERMS.MethodLink, default=None)


class TimeSeriesMethodInRDF(TimeSeriesMethod):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class ProcessingLevel(BaseModel):
    processing_level_code: str = Field(rdf_predicate=HSTERMS.ProcessingLevelCode)
    definition: str = Field(rdf_predicate=HSTERMS.Definition, default=None)
    explanation: str = Field(rdf_predicate=HSTERMS.Explanation, default=None)


class ProcessingLevelInRDF(ProcessingLevel):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class Unit(BaseModel):
    type: str = Field(rdf_predicate=HSTERMS.UnitsType)
    name: str = Field(rdf_predicate=HSTERMS.UnitsName)
    abbreviation: str = Field(rdf_predicate=HSTERMS.UnitsAbbreviation)


class UnitInRDF(Unit):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class UTCOffSet(BaseModel):
    value: str = Field(rdf_predicate=HSTERMS.value)


class UTCOffSetInRDF(UTCOffSet):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)


class TimeSeriesResult(BaseModel):
    series_id: str = Field(rdf_predicate=HSTERMS.timeSeriesResultUUID)
    unit: Unit = Field(rdf_predicate=HSTERMS.unit, default=None)
    status: str = Field(rdf_predicate=HSTERMS.Status, default=None)
    sample_medium: str = Field(rdf_predicate=HSTERMS.SampleMedium)
    value_count: int = Field(rdf_predicate=HSTERMS.ValueCount)
    aggregation_statistics: str = Field(rdf_predicate=HSTERMS.AggregationStatistic)
    series_label: str = Field(rdf_predicate=HSTERMS.SeriesLabel, default=None)
    site: TimeSeriesSite = Field(rdf_predicate=HSTERMS.site)
    variable: TimeSeriesVariable = Field(rdf_predicate=HSTERMS.variable)
    method: TimeSeriesMethod = Field(rdf_predicate=HSTERMS.method)
    processing_level: ProcessingLevel = Field(rdf_predicate=HSTERMS.processingLevel)
    utc_offset: UTCOffSet = Field(rdf_predicate=HSTERMS.UTCOffSet, default=None)


class TimeSeriesResultInRDF(TimeSeriesResult):
    rdf_subject: RDFIdentifier = Field(default_factory=BNode)

    unit: UnitInRDF = Field(rdf_predicate=HSTERMS.unit, default=None)
    site: TimeSeriesSiteInRDF = Field(rdf_predicate=HSTERMS.site)
    variable: TimeSeriesVariableInRDF = Field(rdf_predicate=HSTERMS.variable)
    method: TimeSeriesMethodInRDF = Field(rdf_predicate=HSTERMS.method)
    processing_level: ProcessingLevelInRDF = Field(rdf_predicate=HSTERMS.processingLevel)
    utc_offset: UTCOffSetInRDF = Field(rdf_predicate=HSTERMS.UTCOffSet, default=None)
