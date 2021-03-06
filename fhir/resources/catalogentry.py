# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CatalogEntry(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An entry in a catalog.
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """

    resource_type = Field("CatalogEntry", const=True)

    additionalCharacteristic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="additionalCharacteristic",
        title="Additional characteristics of the catalog entry",
        description="Used for examplefor Out of Formulary, or any specifics.",
        # if property is element of this resource.
        element_property=True,
    )

    additionalClassification: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="additionalClassification",
        title="Additional classification of the catalog entry",
        description="User for example for ATC classification, or.",
        # if property is element of this resource.
        element_property=True,
    )

    additionalIdentifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="additionalIdentifier",
        title=(
            "Any additional identifier(s) for the catalog item, in the same "
            "granularity or concept"
        ),
        description="Used in supporting related concepts, e.g. NDC to RxNorm.",
        # if property is element of this resource.
        element_property=True,
    )

    classification: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="classification",
        title="Classification (category or class) of the item entry",
        description="Classes of devices, or ATC for medication.",
        # if property is element of this resource.
        element_property=True,
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier of the catalog item",
        description=(
            "Used in supporting different identifiers for the same product, e.g. "
            "manufacturer code and retailer code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    lastUpdated: fhirtypes.DateTime = Field(
        None,
        alias="lastUpdated",
        title="When was this catalog last updated",
        description=(
            "Typically date of issue is different from the beginning of the "
            "validity. This can be used to see when an item was last updated."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastUpdated", title="Extension field for ``lastUpdated``."
    )

    orderable: bool = Field(
        ...,
        alias="orderable",
        title="Whether the entry represents an orderable item",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    orderable__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_orderable", title="Extension field for ``orderable``."
    )

    referencedItem: fhirtypes.ReferenceType = Field(
        ...,
        alias="referencedItem",
        title="The item that is being defined",
        description="The item in a catalog or definition.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Medication",
            "Device",
            "Organization",
            "Practitioner",
            "PractitionerRole",
            "HealthcareService",
            "ActivityDefinition",
            "PlanDefinition",
            "SpecimenDefinition",
            "ObservationDefinition",
            "Binary",
        ],
    )

    relatedEntry: ListType[fhirtypes.CatalogEntryRelatedEntryType] = Field(
        None,
        alias="relatedEntry",
        title="An item that this catalog entry is related to",
        description=(
            "Used for example, to point to a substance, or to a device used to "
            "administer a medication."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "Used to support catalog exchange even for unsupported products, e.g. "
            "getting list of medications even if not prescribable."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="The type of item - medication, device, service, protocol or other",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    validTo: fhirtypes.DateTime = Field(
        None,
        alias="validTo",
        title="The date until which this catalog entry is expected to be active",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    validTo__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_validTo", title="Extension field for ``validTo``."
    )

    validityPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="validityPeriod",
        title="The time period in which this catalog entry is expected to be active",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )


class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An item that this catalog entry is related to.
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """

    resource_type = Field("CatalogEntryRelatedEntry", const=True)

    item: fhirtypes.ReferenceType = Field(
        ...,
        alias="item",
        title="The reference to the related item",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["CatalogEntry"],
    )

    relationtype: fhirtypes.Code = Field(
        ...,
        alias="relationtype",
        title="triggers | is-replaced-by",
        description=(
            "The type of relation to the related item: child, parent, "
            "packageContent, containerPackage, usedIn, uses, requires, etc."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["triggers", "is-replaced-by"],
    )
    relationtype__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relationtype", title="Extension field for ``relationtype``."
    )
