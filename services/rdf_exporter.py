from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, DCTERMS

def generate_rdf(metadata):
    g = Graph()

    DCAT = Namespace("http://www.w3.org/ns/dcat#")
    EX = Namespace("http://example.org/")

    dataset = EX["dataset"]

    g.add((dataset, RDF.type, DCAT.Dataset))

    if metadata.get("title"):
        g.add((dataset, DCTERMS.title, Literal(metadata["title"])))

    if metadata.get("description"):
        g.add((dataset, DCTERMS.description, Literal(metadata["description"])))

    for keyword in metadata.get("keywords", []):
        g.add((dataset, DCAT.keyword, Literal(keyword)))

    if metadata.get("format"):
        g.add((dataset, DCTERMS.format, Literal(metadata["format"])))

    if metadata.get("mediaType"):
        g.add((dataset, DCAT.mediaType, Literal(metadata["mediaType"])))

    if metadata.get("theme"):
        g.add((dataset, DCAT.theme, Literal(metadata["theme"])))

    if metadata.get("creator", {}).get("@id"):
        g.add((dataset, DCTERMS.creator, URIRef(metadata["creator"]["@id"])))

    if metadata.get("license", {}).get("@id"):
        g.add((dataset, DCTERMS.license, URIRef(metadata["license"]["@id"])))

    if metadata.get("issued"):
        g.add((dataset, DCTERMS.issued, Literal(metadata["issued"])))

    if metadata.get("modified"):
        g.add((dataset, DCTERMS.modified, Literal(metadata["modified"])))

    if metadata.get("language"):
        g.add((dataset, DCTERMS.language, Literal(metadata["language"])))

    if metadata.get("spatial"):
        g.add((dataset, DCTERMS.spatial, Literal(metadata["spatial"])))

    if metadata.get("temporal"):
        g.add((dataset, DCTERMS.temporal, Literal(metadata["temporal"])))

    if metadata.get("accrualPeriodicity"):
        g.add((dataset, DCTERMS.accrualPeriodicity, Literal(metadata["accrualPeriodicity"])))

    return g.serialize(format="turtle")