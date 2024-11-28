grammar segno_grammar;	
    
// ------------------------------
//      tokens
// ------------------------------

NEWLINE         : [\r\n]+              -> channel( HIDDEN );
WHITESPACE      : [ \n\t\r]+           -> channel( HIDDEN );
COMMENT         : '#' ~('\r' | '\n' )* -> channel( HIDDEN );

// brackets
TOKEN_CURL_LH   : '{' ;
TOKEN_CURL_RH   : '}' ;
TOKEN_SQUARE_LH : '[' ;
TOKEN_SQUARE_RH : ']' ;
TOKEN_ROUND_LH  : '(' ;
TOKEN_ROUND_RH  : ')' ;
TOKEN_ANG_LH    : '<' ;
TOKEN_ANG_RH    : '>' ;

// operators
TOKEN_ARROW_LW  : '<-'  ;
TOKEN_ARROW_RW  : '->'  ;
TOKEN_ARROW_SYM : '<->' ;
TOKEN_IPLMAP_LW : ':<'  ;
TOKEN_IPLMAP_RW : ':>'  ;
TOKEN_PLUS      : '+'   ;
TOKEN_MINUS     : '-'   ;
TOKEN_DCOLON    : '::'  ;
TOKEN_DDOT      : '..'  ;

// useful keywords
KEYWORD_FIELD    : 'field'    ;
KEYWORD_OPERATOR : 'operator' ;
KEYWORD_PASS     : 'pass'     ;

// intrinsic
KEYWORD_BOOL    : 'bool'  ;
TOKEN_TRUE      : 'true'  ;
TOKEN_FALSE     : 'false' ;

IDENTIFIER
    : FRAG_NONDIGIT (FRAG_NONDIGIT | FRAG_DIGIT)*
    ;
    
FRAG_DEC_NAT_NUMBER
    : FRAG_DIGIT+
    ;

FRAG_NONDIGIT        : [a-zA-Z_] ;
FRAG_DIGIT           : [0-9]     ;

// ------------------------------
//    prog
// ------------------------------

prog
    : prog_element* EOF
    ;

prog_element
    : field_def
    | operator_def
    | pass_def
    ;
    
// ------------------------------
//      fields
// ------------------------------

field_def
    : KEYWORD_FIELD identifier
    ;
    
// ------------------------------
//      operators
// ------------------------------

operator_def
    : KEYWORD_OPERATOR identifier
    ;
    
// ------------------------------
//      passes
// ------------------------------

pass_def
    : KEYWORD_PASS identifier
      TOKEN_CURL_LH
      pass_element_def*
      TOKEN_CURL_RH
    ;

pass_element_def
    : IDENTIFIER
    ;
    
// ------------------------------
//      identifiers
// ------------------------------

identifier_name
    : IDENTIFIER
    ;

identifier
    : identifier_name
    ;
