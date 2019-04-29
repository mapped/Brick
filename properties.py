from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
TAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
A = RDF.type


"""
Defining properties
"""
properties = {
    "isLocationOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "hasLocation",
        RDFS.domain: BRICK.Location,
    },
    "hasLocation": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "isLocationOf",
        RDFS.range: BRICK.Location,
    },

    "hasInputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
    },
    "hasOutputSubstance": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.range: BRICK.Substance,
    },

    "controls": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "isControlledBy",
    },
    "isControlledBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "controls",
    },


    "feeds": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "isFedBy",
        "subproperties": {
            "feedsAir": {
                SKOS.definition: Literal("Passes air"),


                # TODO: add restriction that it needs an air-based equipment on either side?
                # this is equivalent with the classes that have :
                # Restriction (onProperty=brick:hasInputSubstance, hasValue=brick:Air) AND
                # Restriction (onProperty=brick:hasOutputSubstance, hasValue=brick:Air)

                # looks something like this
                #"domain_value_prop": [
                #    [BRICK.hasTag, TAG.Air],
                #],
                #"range_value_prop": [
                #    [BRICK.hasTag, TAG.Air],
                #],
            },
        },
    },
    "isFedBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "feeds",
    },

    "hasPoint": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "isPointOf",
        RDFS.range: BRICK.Point,
    },
    "isPointOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "hasPoint",
        RDFS.domain: BRICK.Point,
    },

    "hasPart": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "isPartOf",
    },
    "isPartOf": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "hasPart",
    },

    "hasTag": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "isTagOf",
        RDFS.range: BRICK.Tag,
    },

    "measures": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: "isMeasuredBy",
        RDFS.domain: BRICK.Point,
        RDFS.range: BRICK.Substance,
    },
    "isMeasuredBy": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.domain: BRICK.Substance,
        RDFS.range: BRICK.Point,
    },

    # Haystack-style
    "ahuRef": {
        RDFS.range: BRICK.AHU,
    }
}
