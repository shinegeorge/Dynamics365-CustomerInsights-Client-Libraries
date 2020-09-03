# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AttributeType(Model):
    """Represents a property type backed by an EDM type and a CLR type. Enables
    conversion of values from strings, as
    well as various other type-based operations.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar clr_type: Gets the CLR Type for this property type.
    :vartype clr_type: str
    :param cdsa_type: Possible values include: 'unclassified', 'string',
     'int64', 'double', 'dateTime', 'dateTimeOffset', 'decimal', 'boolean',
     'guid', 'json'
    :type cdsa_type: str or ~dynamics.customerinsights.api.models.enum
    :ivar edm_type_name: Gets the EDM type name for the property type, in the
     format EdmTypeKind>".
    :vartype edm_type_name: str
    :ivar is_boolean:
    :vartype is_boolean: bool
    :ivar is_date_time:
    :vartype is_date_time: bool
    :ivar is_decimal:
    :vartype is_decimal: bool
    :ivar is_number:
    :vartype is_number: bool
    :ivar is_valid_type: Gets a value indicating whether this type valid and
     supported by the runtime.
    :vartype is_valid_type: bool
    :ivar name: Gets the name of the property type. Will default to the
     EdmTypeName but may be overridden by a property
     type.
    :vartype name: str
    :param equality_comparer:
    :type equality_comparer: object
    :param comparer:
    :type comparer: object
    :param o_data_type:
    :type o_data_type: ~dynamics.customerinsights.api.models.IEdmType
    :ivar is_collection:
    :vartype is_collection: bool
    """

    _validation = {
        'clr_type': {'readonly': True},
        'edm_type_name': {'readonly': True},
        'is_boolean': {'readonly': True},
        'is_date_time': {'readonly': True},
        'is_decimal': {'readonly': True},
        'is_number': {'readonly': True},
        'is_valid_type': {'readonly': True},
        'name': {'readonly': True},
        'is_collection': {'readonly': True},
    }

    _attribute_map = {
        'clr_type': {'key': 'clrType', 'type': 'str'},
        'cdsa_type': {'key': 'cdsaType', 'type': 'str'},
        'edm_type_name': {'key': 'edmTypeName', 'type': 'str'},
        'is_boolean': {'key': 'isBoolean', 'type': 'bool'},
        'is_date_time': {'key': 'isDateTime', 'type': 'bool'},
        'is_decimal': {'key': 'isDecimal', 'type': 'bool'},
        'is_number': {'key': 'isNumber', 'type': 'bool'},
        'is_valid_type': {'key': 'isValidType', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'equality_comparer': {'key': 'equalityComparer', 'type': 'object'},
        'comparer': {'key': 'comparer', 'type': 'object'},
        'o_data_type': {'key': 'oDataType', 'type': 'IEdmType'},
        'is_collection': {'key': 'isCollection', 'type': 'bool'},
    }

    def __init__(self, *, cdsa_type=None, equality_comparer=None, comparer=None, o_data_type=None, **kwargs) -> None:
        super(AttributeType, self).__init__(**kwargs)
        self.clr_type = None
        self.cdsa_type = cdsa_type
        self.edm_type_name = None
        self.is_boolean = None
        self.is_date_time = None
        self.is_decimal = None
        self.is_number = None
        self.is_valid_type = None
        self.name = None
        self.equality_comparer = equality_comparer
        self.comparer = comparer
        self.o_data_type = o_data_type
        self.is_collection = None
