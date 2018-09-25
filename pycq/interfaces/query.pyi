from typing import Generic, List, TypeVar, Iterable, overload, Callable, Dict, Set, Tuple, Type, AnyStr, FrozenSet, \
    Deque

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TOther = TypeVar('TOther')
TItem = TypeVar('TItem')


class NumberedItem(Generic[T]):
    @property
    def no(self) -> int: ...

    @property
    def item(self) -> T: ...


class GroupedItems(Generic[TKey, T]):
    @property
    def key(self) -> TKey: ...

    @property
    def items(self) -> "Query[T]": ...


class ZippedItems(Generic[T, TOther]):
    @property
    def left(self) -> T: ...

    @property
    def right(self) -> TOther: ...


class JoinedItems(Generic[TKey, T, TOther]):
    @property
    def key(self) -> TKey: ...

    @property
    def left(self) -> T: ...

    @property
    def right(self) -> TOther: ...


class GroupJoinedItems(Generic[TKey, T, TOther]):
    @property
    def key(self) -> TKey: ...

    @property
    def left_items(self) -> "Query[T]": ...

    @property
    def right_items(self) -> "Query[T]": ...


class Query(Generic[T], Iterable[T]):
    def __query__(self) -> "Query[T]": ...

    def tee(self) -> "Query[T]": ...
    def with_number(self) -> "Query[NumberedItem[T]]": ...
    @overload
    def reduce(self, func: Callable[[T, T], T]) -> T: ...
    @overload
    def reduce(self, initializer: TValue, func: Callable[[TValue, T], TValue]) -> TValue: ...
    def select(self, selector: Callable[[T], TValue]) -> "Query[TValue]": ...
    def select_many(self, selector: Callable[[T], Iterable[TValue]]) -> "Query[TValue]": ...
    def chain(self: "Query[Iterable[TItem]]") -> "Query[TItem]": ...
    def where(self, condition: Callable[[T], bool]) -> "Query[T]": ...
    def cast(self, type: Type[TValue]) -> "Query[TValue]": ...
    def of_type(self, type: Type[TValue]) -> "Query[TValue]": ...
    def distinct(self, key_selector: Callable[[T], bool] = None) -> "Query[T]": ...
    def union(self, iterable: Iterable[T]) -> "Query[T]": ...
    def intersect(self, iterable: Iterable[T]) -> "Query[T]": ...
    def except_(self, iterable: Iterable[T]) -> "Query[T]": ...
    def distinct_ordered(self, key_selector: Callable[[T], bool] = None) -> "Query[T]": ...
    def count(self) -> int: ...
    @overload
    def sum(self) -> T: ...
    @overload
    def sum(self, selector: Callable[[T], TValue]) -> TValue: ...
    @overload
    def average(self) -> TValue: ...
    @overload
    def average(self, selector: Callable[[T], TValue]) -> TValue: ...
    def average(self, selector=None): ...
    @overload
    def min(self) -> T: ...
    @overload
    def min(self, selector: Callable[[T], TValue]) -> TValue: ...
    def having_min(self, selector: Callable[[T], TValue]) -> "Query[T]": ...
    @overload
    def max(self) -> T: ...
    @overload
    def max(self, selector: Callable[[T], TValue]) -> TValue: ...
    def having_max(self, selector: Callable[[T], TValue]) -> "Query[T]": ...
    @overload
    def first(self) -> T: ...
    @overload
    def first(self, condition: Callable[[T], bool]) -> T: ...
    @overload
    def first_or_default(self, default: T) -> T: ...
    @overload
    def first_or_default(self, default: T, condition: Callable[[T], bool]) -> T: ...
    @overload
    def last(self) -> T: ...
    @overload
    def last(self, condition: Callable[[T], bool]) -> T: ...
    @overload
    def last_or_default(self, default: T) -> T: ...
    @overload
    def last_or_default(self, default: T, condition: Callable[[T], bool]) -> T: ...
    def skip(self, count: int) -> "Query[T]": ...
    def skip_while(self, condition: Callable[[T], bool]) -> "Query[T]": ...
    def skip_last(self, count: int) -> "Query[T]": ...
    def skip_last_having(self, condition: Callable[[T], bool]) -> "Query[T]": ...
    def take(self, count: int) -> "Query[T]": ...
    def take_while(self, condition: Callable[[T], bool]) -> "Query[T]": ...
    def take_last(self, count: int) -> "Query[T]": ...
    def take_last_having(self, condition: Callable[[T], bool]) -> "Query[T]": ...
    def any(self, condition: Callable[[T], bool] = None) -> bool: ...
    def all(self, condition: Callable[[T], bool]) -> bool: ...
    def contains(self, value: T) -> bool: ...
    def contains_all(self, iterable: Iterable[T]) -> bool: ...
    def contains_any(self, iterable: Iterable[T]) -> bool: ...
    def sequence_equal(self, iterable: Iterable[T]) -> bool: ...
    def default_if_empty(self, default: T) -> "Query[T]": ...
    def prepend_all(self, iterable: Iterable[T]) -> "Query[T]": ...
    def prepend(self, value: T) -> "Query[T]": ...
    def append_all(self, iterable: Iterable[T]) -> "Query[T]": ...
    def append(self, value: T) -> "Query[T]": ...
    def group_by(self, key_selector: Callable[[T], TKey]) -> "Query[GroupedItems[TKey, T]]": ...
    def group_by_ordered(self, key_selector: Callable[[T], TKey]) -> "Query[GroupedItems[TKey, T]]": ...
    def sort_by(self, key_selector: Callable[[T], TKey]) -> "SortingQuery[T]": ...
    def sort_by_desc(self, key_selector: Callable[[T], TKey]) -> "SortingQuery[T]": ...
    def reverse(self) -> "Query[T]": ...
    def zip(self, other_iterable: Iterable[TOther]) -> "Query[ZippedItems[T, TOther]]": ...
    @overload
    def zip_longest(self, other_iterable: Iterable[TOther], *, fill_left: T = None, fill_right: TOther = None)\
            -> "Query[ZippedItems[T, TOther]]": ...
    @overload
    def zip_longest(self, other_iterable: Iterable[T], *, fill: T = None)\
            -> "Query[ZippedItems[T, T]]": ...
    def inner_join(self, other_iterable: Iterable[TOther], left_key_selector: Callable[[T], TKey],
             right_key_selector: Callable[[T], TKey]) -> "Query[JoinedItems[TKey, T, TOther]]": ...
    def group_join(self, other_iterable: Iterable[TOther], left_key_selector: Callable[[T], TKey],
             right_key_selector: Callable[[T], TKey]) -> "Query[GroupJoinedItems[TKey, T, TOther]]": ...
    def to_list(self) -> List[T]: ...
    def to_set(self) -> Set[T]: ...
    def to_frozenset(self) -> FrozenSet[T]: ...
    def to_tuple(self) -> Tuple[T, ...]: ...
    @overload
    def to_dict(self, key_selector: Callable[[T], TKey]) -> Dict[TKey, T]: ...
    @overload
    def to_dict(self, key_selector: Callable[[T], TKey], value_selector: Callable[[T], TValue]) -> Dict[TKey, TValue]: ...
    def to_deque(self, max_length: int = None) -> Deque[T]: ...
    def join(self: "Query[AnyStr]", separator: AnyStr) -> AnyStr: ...


class SortingQuery(Generic[T], Query[T]):
    def then_by(self, key_selector: Callable[[T], TKey]) -> "SortingQuery[T]": ...
    def then_by_desc(self, key_selector: Callable[[T], TKey]) -> "SortingQuery[T]": ...