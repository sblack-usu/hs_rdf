import uuid
from datetime import datetime
from typing import List, Union, Dict

from pydantic import Field, AnyUrl, validator, root_validator

from hs_rdf.namespaces import HSRESOURCE, HSTERMS, RDF, DC, ORE, CITOTERMS
from hs_rdf.schemas.base_models import BaseMetadata, RDFBaseModel
from hs_rdf.schemas.constraints import language_constraint, dates_constraint, coverages_constraint, \
    coverages_spatial_constraint
from hs_rdf.schemas.fields import DescriptionInRDF, CreatorInRDF, ContributorInRDF, SourceInRDF, \
    RelationInRDF, ExtendedMetadataInRDF, RightsInRDF, DateInRDF, AwardInfoInRDF, CoverageInRDF, IdentifierInRDF, \
    PublisherInRDF, BoxCoverage, PeriodCoverage, PointCoverage
from rdflib.term import Identifier as RDFIdentifier

from hs_rdf.schemas.root_validators import parse_coverages, parse_rdf_extended_metadata, parse_rdf_dates, \
    rdf_parse_description, rdf_parse_rdf_subject
from hs_rdf.schemas.validators import parse_additional_metadata, parse_period_coverage, parse_spatial_coverage, \
    parse_identifier, parse_abstract, parse_created, parse_modified, parse_published, parse_sources, \
    rdf_parse_identifier, parse_rdf_sources


def hs_uid():
    return getattr(HSRESOURCE, uuid.uuid4().hex)


class ResourceMetadataInRDF(RDFBaseModel):
    rdf_subject: RDFIdentifier = Field(default_factory=hs_uid)
    _parse_rdf_subject = root_validator(pre=True, allow_reuse=True)(rdf_parse_rdf_subject)

    rdf_type: AnyUrl = Field(rdf_predicate=RDF.type, const=True, default=HSTERMS.CompositeResource)

    label: str = Field(default="Composite Resource", const=True)

    title: str = Field(rdf_predicate=DC.title)
    description: DescriptionInRDF = Field(rdf_predicate=DC.description, default_factory=DescriptionInRDF)
    language: str = Field(rdf_predicate=DC.language, default='eng')
    subjects: List[str] = Field(rdf_predicate=DC.subject, default=[])
    dc_type: AnyUrl = Field(rdf_predicate=DC.type, default=HSTERMS.CompositeResource, const=True)
    identifier: IdentifierInRDF = Field(rdf_predicate=DC.identifier)
    creators: List[CreatorInRDF] = Field(rdf_predicate=DC.creator)

    contributors: List[ContributorInRDF] = Field(rdf_predicate=DC.contributor, default=[])
    sources: List[SourceInRDF] = Field(rdf_predicate=DC.source, default=[])
    relations: List[RelationInRDF] = Field(rdf_predicate=DC.relation, default=[])
    extended_metadata: List[ExtendedMetadataInRDF] = Field(rdf_predicate=HSTERMS.extendedMetadata, default=[])
    rights: RightsInRDF = Field(rdf_predicate=DC.rights, default=None)
    dates: List[DateInRDF] = Field(rdf_predicate=DC.date)
    award_infos: List[AwardInfoInRDF] = Field(rdf_predicate=HSTERMS.awardInfo, default=[])
    coverages: List[CoverageInRDF] = Field(rdf_predicate=DC.coverage, default=[])
    publisher: PublisherInRDF = Field(rdf_predicate=DC.publisher, default=None)

    _parse_coverages = root_validator(pre=True, allow_reuse=True)(parse_coverages)
    _parse_extended_metadata = root_validator(pre=True, allow_reuse=True)(parse_rdf_extended_metadata)
    _parse_rdf_dates = root_validator(pre=True, allow_reuse=True)(parse_rdf_dates)
    _parse_description = root_validator(pre=True, allow_reuse=True)(rdf_parse_description)

    _parse_identifier = validator("identifier", pre=True, allow_reuse=True)(rdf_parse_identifier)
    _parse_rdf_sources = validator("sources", pre=True, allow_reuse=True)(parse_rdf_sources)

    _language_constraint = validator('language', allow_reuse=True)(language_constraint)
    _dates_constraint = validator('dates', allow_reuse=True)(dates_constraint)
    _coverages_constraint = validator('coverages', allow_reuse=True)(coverages_constraint)
    _coverages_spatial_constraint = validator('coverages', allow_reuse=True)(coverages_spatial_constraint)


class Creator(RDFBaseModel):
    name: str = Field(description="The name of a creator", default=None)

    creator_order: int = Field(description="the order the creator will appear")
    email: str = Field(default=None, description="the email of a creator")
    organization: str = Field(default=None, description="the organization of the creator")


class ResourceMetadata(BaseMetadata):
    _rdf_model_class = ResourceMetadataInRDF

    url: AnyUrl = Field(alias="rdf_subject")

    identifier: AnyUrl
    title: str = Field(default=None, description="The description of a title")
    abstract: str = Field(alias="description", default=None)
    language: str
    subjects: List[str] = []
    creators: List[Creator] = Field(default=[], description="A list of creators")
    contributors: List[ContributorInRDF] = []
    sources: List[str] = Field(default=[])
    relations: List[RelationInRDF] = Field(default=[])
    additional_metadata: Dict[str, str] = Field(alias="extended_metadata", default={})
    rights: RightsInRDF = Field(default=None)
    created: datetime = Field(alias="dates", default_factory=datetime.now)
    modified: datetime = Field(alias="dates", default_factory=datetime.now)
    published: datetime = Field(alias="dates", default=None)
    award_infos: List[AwardInfoInRDF] = Field(default=[])
    spatial_coverage: Union[BoxCoverage, PointCoverage] = Field(alias='coverages', default=None)
    period_coverage: PeriodCoverage = Field(alias='coverages', default=None)
    publisher: PublisherInRDF = Field(default=None)

    _parse_additional_metadata = validator("additional_metadata", pre=True, allow_reuse=True)(parse_additional_metadata)
    _parse_spatial_coverage = validator("spatial_coverage", pre=True, allow_reuse=True)(parse_spatial_coverage)
    _parse_period_coverage = validator("period_coverage", pre=True, allow_reuse=True)(parse_period_coverage)

    _parse_identifier = validator("identifier", pre=True)(parse_identifier)
    _parse_abstract = validator("abstract", pre=True)(parse_abstract)
    _parse_created = validator("created", pre=True)(parse_created)
    _parse_modified = validator("modified", pre=True)(parse_modified)
    _parse_published = validator("published", pre=True)(parse_published)
    _parse_sources = validator("sources", pre=True)(parse_sources)

    _language_constraint = validator('language', allow_reuse=True)(language_constraint)


class FileMap(RDFBaseModel):
    rdf_type: AnyUrl = Field(rdf_predicate=RDF.type, const=True, default=ORE.Aggregation)

    is_documented_by: AnyUrl = Field(rdf_predicate=CITOTERMS.isDocumentedBy)
    files: List[AnyUrl] = Field(rdf_predicate=ORE.aggregates)
    title: str = Field(rdf_predicate=DC.title)
    is_described_by: AnyUrl = Field(rdf_predicate=ORE.isDescribedBy)


class ResourceMap(RDFBaseModel):
    rdf_type: AnyUrl = Field(rdf_predicate=RDF.type, const=True, default=ORE.ResourceMap)

    describes: FileMap = Field(rdf_predicate=ORE.describes)
    identifier: str = Field(rdf_predicate=DC.identifier, default=None)
    #modified: datetime = Field(rdf_predicate=DCTERMS.modified)
    creator: str = Field(rdf_predicate=DC.creator, default=None)
