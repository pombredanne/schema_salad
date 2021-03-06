# Stubs for rdflib.graph (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Union, IO, Tuple, Iterator
from StringIO import StringIO as BytesIO
from rdflib.term import Node, URIRef
from rdflib.store import Store
from rdflib.namespace import NamespaceManager
from rdflib.query import Result

class Graph(Node):
    context_aware = ... # type: Any
    formula_aware = ... # type: Any
    default_union = ... # type: Any
    def __init__(self, store: Union[Store, str]='default', identifier: Node=None, namespace_manager: NamespaceManager=None) -> None: ... 
    store = ... # type: Any
    identifier = ... # type: Any
    namespace_manager = ... # type: Any
    def toPython(self): ...
    def destroy(self, configuration): ...
    def commit(self): ...
    def rollback(self): ...
    def open(self, configuration, create=False): ...
    def close(self, commit_pending_transaction=False): ...
    def add(self, __tuple_arg_2: Tuple[Node, Node, Node]) -> None: ...
    def addN(self, quads): ...
    def remove(self, __tuple_arg_2): ...
    def triples(self, __tuple_arg_2: Tuple[Union[str, URIRef], str, Union[str, URIRef]]) -> Iterator[Tuple[str, str, str]]: ...
    def __getitem__(self, item): ...
    def __len__(self): ...
    def __iter__(self): ...
    def __contains__(self, triple): ...
    def __hash__(self): ...
    def md5_term_hash(self): ...
    def __cmp__(self, other): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __iadd__(self, other): ...
    def __isub__(self, other): ...
    def __add__(self, other): ...
    def __mul__(self, other): ...
    def __sub__(self, other): ...
    def __xor__(self, other): ...
    __or__ = ... # type: Any
    __and__ = ... # type: Any
    def set(self, triple): ...
    def subjects(self, predicate=None, object=None): ...
    def predicates(self, subject=None, object=None): ...
    def objects(self, subject=None, predicate=None): ...
    def subject_predicates(self, object=None): ...
    def subject_objects(self, predicate=None): ...
    def predicate_objects(self, subject=None): ...
    def triples_choices(self, __tuple_arg_2, context=None): ...
    def value(self, subject=None, predicate=..., object=None, default=None, any=True): ...
    def label(self, subject, default=''): ...
    def preferredLabel(self, subject, lang=None, default=None, labelProperties=...): ...
    def comment(self, subject, default=''): ...
    def items(self, list): ...
    def transitiveClosure(self, func, arg, seen=None): ...
    def transitive_objects(self, subject, property, remember=None): ...
    def transitive_subjects(self, predicate, object, remember=None): ...
    def seq(self, subject): ...
    def qname(self, uri): ...
    def compute_qname(self, uri, generate=True): ...
    def bind(self, prefix: str, namespace: str, override: bool=True) -> None: ...
    def namespaces(self): ...
    def absolutize(self, uri, defrag=1): ...
    def serialize(self, destination: Union[str, IO[Any]]=None, format: str='', base: str=None, encoding: str=None, **args) -> Union[bytes, None]: ...
    def parse(self, source: str = None, publicID: str = None,
              format: Union[str, unicode] = None,
              location: Union[str, unicode] = None, file: IO[Any] = None,
              data: str = None, **args): ...
    def load(self, source, publicID=None, format=''): ...
    def query(self, query_object, processor: str = '', result: str = '', initNs: Dict = None, initBindings: Dict = None, use_store_provided: bool = True, **kwargs) -> Result: ...
    def update(self, update_object, processor='', initNs=..., initBindings=..., use_store_provided=True, **kwargs): ...
    def n3(self): ...
    def __reduce__(self): ...
    def isomorphic(self, other): ...
    def connected(self): ...
    def all_nodes(self): ...
    def resource(self, identifier): ...
    def skolemize(self, new_graph=None, bnode=None): ...
    def de_skolemize(self, new_graph=None, uriref=None): ...

class ConjunctiveGraph(Graph):
    context_aware = ... # type: Any
    default_union = ... # type: Any
    default_context = ... # type: Any
    def __init__(self, store='', identifier=None): ...
    def __contains__(self, triple_or_quad): ...
    def add(self, triple_or_quad): ...
    def addN(self, quads): ...
    def remove(self, triple_or_quad): ...
    def triples(self, triple_or_quad, context=None): ...
    def quads(self, triple_or_quad=None): ...
    def triples_choices(self, __tuple_arg_2, context=None): ...
    def __len__(self): ...
    def contexts(self, triple=None): ...
    def get_context(self, identifier, quoted=False): ...
    def remove_context(self, context): ...
    def context_id(self, uri, context_id=None): ...
    def parse(self, source=None, publicID=None, format='', location=None, file=None, data=None, **args): ...
    def __reduce__(self): ...

class Dataset(ConjunctiveGraph):
    __doc__ = ... # type: Any
    default_context = ... # type: Any
    default_union = ... # type: Any
    def __init__(self, store='', default_union=False): ...
    def graph(self, identifier=None): ...
    def parse(self, source=None, publicID=None, format='', location=None, file=None, data=None, **args): ...
    def add_graph(self, g): ...
    def remove_graph(self, g): ...
    def contexts(self, triple=None): ...
    def quads(self, quad): ...

class QuotedGraph(Graph):
    def __init__(self, store, identifier): ...
    def add(self, __tuple_arg_2): ...
    def addN(self, quads): ...
    def n3(self): ...
    def __reduce__(self): ...

class Seq:
    def __init__(self, graph, subject): ...
    def toPython(self): ...
    def __iter__(self): ...
    def __len__(self): ...
    def __getitem__(self, index): ...

class ModificationException(Exception):
    def __init__(self): ...

class UnSupportedAggregateOperation(Exception):
    def __init__(self): ...

class ReadOnlyGraphAggregate(ConjunctiveGraph):
    graphs = ... # type: Any
    def __init__(self, graphs, store=''): ...
    def destroy(self, configuration): ...
    def commit(self): ...
    def rollback(self): ...
    def open(self, configuration, create=False): ...
    def close(self): ...
    def add(self, __tuple_arg_2): ...
    def addN(self, quads): ...
    def remove(self, __tuple_arg_2): ...
    def triples(self, __tuple_arg_2): ...
    def __contains__(self, triple_or_quad): ...
    def quads(self, __tuple_arg_2): ...
    def __len__(self): ...
    def __hash__(self): ...
    def __cmp__(self, other): ...
    def __iadd__(self, other): ...
    def __isub__(self, other): ...
    def triples_choices(self, __tuple_arg_2, context=None): ...
    def qname(self, uri): ...
    def compute_qname(self, uri, generate=True): ...
    def bind(self, prefix, namespace, override=True): ...
    def namespaces(self): ...
    def absolutize(self, uri, defrag=1): ...
    def parse(self, source, publicID=None, format='', **args): ...
    def n3(self): ...
    def __reduce__(self): ...
