from cerberus import Validator

TABLE_PARAM_RULE = {
    "type": "string",
    "required": False,
    "empty": False
}
INTEGER_PARAM_RULE = {
    "type": "integer",
    "required": True
}
OPTIONAL_INTEGER_PARAM_RULE = {
    "type": "integer",
    "required": False
}
ANY_PARAM_RULE = {
    "required": True
}

GET_PARAM_SCHEMA = {
    "table": TABLE_PARAM_RULE,
    "index": OPTIONAL_INTEGER_PARAM_RULE,
    "from_i": OPTIONAL_INTEGER_PARAM_RULE,
    "to_i": OPTIONAL_INTEGER_PARAM_RULE
}

ADD_PARAM_SCHEMA = {
    "table": TABLE_PARAM_RULE,
    "value": ANY_PARAM_RULE
}

UPDATE_PARAM_SCHEMA = {
    "table": TABLE_PARAM_RULE,
    "index": INTEGER_PARAM_RULE,
    "value": ANY_PARAM_RULE
}

DELETE_PARAM_SCHEMA = {
    "table": TABLE_PARAM_RULE,
    "index": INTEGER_PARAM_RULE
}
DELETE_TABLE_PARAM_SCHEMA = {
    "table": TABLE_PARAM_RULE
}

QUERY_PARAM_SCHEMA = {
    "table": TABLE_PARAM_RULE,
    "key": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "operator": {
        "type": "string",
        "required": True,
        "allowed": [
            ">", ">=", "<", "<=", "=="
        ]
    },
    "value": ANY_PARAM_RULE
}

get_validator          = Validator(GET_PARAM_SCHEMA)
add_validator          = Validator(ADD_PARAM_SCHEMA)
update_validator       = Validator(UPDATE_PARAM_SCHEMA)
delete_validator       = Validator(DELETE_PARAM_SCHEMA)
delete_table_validator = Validator(DELETE_TABLE_PARAM_SCHEMA)
query_validator        = Validator(QUERY_PARAM_SCHEMA)
