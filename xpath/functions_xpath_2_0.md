https://www.w3.org/TR/xquery-operators/

---

G.1 Functions and Operators by Section
2 Accessors
2.1 fn:node-name
fn:node-name($arg as node()?) as xs:QName?
2.2 fn:nilled
fn:nilled($arg as node()?) as xs:boolean?
2.3 fn:string
fn:string() as xs:string
fn:string($arg as item()?) as xs:string
2.4 fn:data
fn:data($arg as item()*) as xs:anyAtomicType*
2.5 fn:base-uri
fn:base-uri() as xs:anyURI?
fn:base-uri($arg as node()?) as xs:anyURI?
2.6 fn:document-uri
fn:document-uri($arg as node()?) as xs:anyURI?
3 The Error Function
fn:error() as none
fn:error($error as xs:QName) as none
fn:error($error as xs:QName?, $description as xs:string) as none
fn:error($error as xs:QName?, $description as xs:string, $error-object as item()*) as none
4 The Trace Function
fn:trace($value as item()*, $label as xs:string) as item()*
5 Constructor Functions
5.2 A Special Constructor Function for xs:dateTime
fn:dateTime($arg1 as xs:date?, $arg2 as xs:time?) as xs:dateTime?
6 Functions and Operators on Numerics
6.2 Operators on Numeric Values
op:numeric-add($arg1 as numeric, $arg2 as numeric) as numeric
op:numeric-subtract($arg1 as numeric, $arg2 as numeric) as numeric
op:numeric-multiply($arg1 as numeric, $arg2 as numeric) as numeric
op:numeric-divide($arg1 as numeric, $arg2 as numeric) as numeric
op:numeric-integer-divide($arg1 as numeric, $arg2 as numeric) as xs:integer
op:numeric-mod($arg1 as numeric, $arg2 as numeric) as numeric
op:numeric-unary-plus($arg as numeric) as numeric
op:numeric-unary-minus($arg as numeric) as numeric
6.3 Comparison Operators on Numeric Values
op:numeric-equal($arg1 as numeric, $arg2 as numeric) as xs:boolean
op:numeric-less-than($arg1 as numeric, $arg2 as numeric) as xs:boolean
op:numeric-greater-than($arg1 as numeric, $arg2 as numeric) as xs:boolean
6.4 Functions on Numeric Values
fn:abs($arg as numeric?) as numeric?
fn:ceiling($arg as numeric?) as numeric?
fn:floor($arg as numeric?) as numeric?
fn:round($arg as numeric?) as numeric?
fn:round-half-to-even($arg as numeric?) as numeric?
fn:round-half-to-even($arg as numeric?, $precision as xs:integer) as numeric?
7 Functions on Strings
7.2 Functions to Assemble and Disassemble Strings
fn:codepoints-to-string($arg as xs:integer*) as xs:string
fn:string-to-codepoints($arg as xs:string?) as xs:integer*
7.3 Equality and Comparison of Strings
fn:compare($comparand1 as xs:string?, $comparand2 as xs:string?) as xs:integer?
fn:compare($comparand1 as xs:string?, $comparand2 as xs:string?, $collation as xs:string) as xs:integer?
fn:codepoint-equal($comparand1 as xs:string?, $comparand2 as xs:string?) as xs:boolean?
7.4 Functions on String Values
fn:concat($arg1 as xs:anyAtomicType?, $arg2 as xs:anyAtomicType?, ...) as xs:string
fn:string-join($arg1 as xs:string*, $arg2 as xs:string) as xs:string
fn:substring($sourceString as xs:string?, $startingLoc as xs:double) as xs:string
fn:substring($sourceString as xs:string?, $startingLoc as xs:double, $length as xs:double) as xs:string
fn:string-length() as xs:integer
fn:string-length($arg as xs:string?) as xs:integer
fn:normalize-space() as xs:string
fn:normalize-space($arg as xs:string?) as xs:string
fn:normalize-unicode($arg as xs:string?) as xs:string
fn:normalize-unicode($arg as xs:string?, $normalizationForm as xs:string) as xs:string
fn:upper-case($arg as xs:string?) as xs:string
fn:lower-case($arg as xs:string?) as xs:string
fn:translate($arg as xs:string?, $mapString as xs:string, $transString as xs:string) as xs:string
fn:encode-for-uri($uri-part as xs:string?) as xs:string
fn:iri-to-uri($iri as xs:string?) as xs:string
fn:escape-html-uri($uri as xs:string?) as xs:string
7.5 Functions Based on Substring Matching
fn:contains($arg1 as xs:string?, $arg2 as xs:string?) as xs:boolean
fn:contains($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:boolean
fn:starts-with($arg1 as xs:string?, $arg2 as xs:string?) as xs:boolean
fn:starts-with($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:boolean
fn:ends-with($arg1 as xs:string?, $arg2 as xs:string?) as xs:boolean
fn:ends-with($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:boolean
fn:substring-before($arg1 as xs:string?, $arg2 as xs:string?) as xs:string
fn:substring-before($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:string
fn:substring-after($arg1 as xs:string?, $arg2 as xs:string?) as xs:string
fn:substring-after($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:string
7.6 String Functions that Use Pattern Matching
fn:matches($input as xs:string?, $pattern as xs:string) as xs:boolean
fn:matches($input as xs:string?, $pattern as xs:string, $flags as xs:string) as xs:boolean
fn:replace($input as xs:string?, $pattern as xs:string, $replacement as xs:string) as xs:string
fn:replace($input as xs:string?, $pattern as xs:string, $replacement as xs:string, $flags as xs:string) as xs:string
fn:tokenize($input as xs:string?, $pattern as xs:string) as xs:string*
fn:tokenize($input as xs:string?, $pattern as xs:string, $flags as xs:string) as xs:string*
8 Functions on anyURI
8.1 fn:resolve-uri
fn:resolve-uri($relative as xs:string?) as xs:anyURI?
fn:resolve-uri($relative as xs:string?, $base as xs:string) as xs:anyURI?
9 Functions and Operators on Boolean Values
9.1 Additional Boolean Constructor Functions
fn:true() as xs:boolean
fn:false() as xs:boolean
9.2 Operators on Boolean Values
op:boolean-equal($value1 as xs:boolean, $value2 as xs:boolean) as xs:boolean
op:boolean-less-than($arg1 as xs:boolean, $arg2 as xs:boolean) as xs:boolean
op:boolean-greater-than($arg1 as xs:boolean, $arg2 as xs:boolean) as xs:boolean
9.3 Functions on Boolean Values
fn:not($arg as item()*) as xs:boolean
10 Functions and Operators on Durations, Dates and Times
10.4 Comparison Operators on Duration, Date and Time Values
op:yearMonthDuration-less-than($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:boolean
op:yearMonthDuration-greater-than($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:boolean
op:dayTimeDuration-less-than($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:boolean
op:dayTimeDuration-greater-than($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:boolean
op:duration-equal($arg1 as xs:duration, $arg2 as xs:duration) as xs:boolean
op:dateTime-equal($arg1 as xs:dateTime, $arg2 as xs:dateTime) as xs:boolean
op:dateTime-less-than($arg1 as xs:dateTime, $arg2 as xs:dateTime) as xs:boolean
op:dateTime-greater-than($arg1 as xs:dateTime, $arg2 as xs:dateTime) as xs:boolean
op:date-equal($arg1 as xs:date, $arg2 as xs:date) as xs:boolean
op:date-less-than($arg1 as xs:date, $arg2 as xs:date) as xs:boolean
op:date-greater-than($arg1 as xs:date, $arg2 as xs:date) as xs:boolean
op:time-equal($arg1 as xs:time, $arg2 as xs:time) as xs:boolean
op:time-less-than($arg1 as xs:time, $arg2 as xs:time) as xs:boolean
op:time-greater-than($arg1 as xs:time, $arg2 as xs:time) as xs:boolean
op:gYearMonth-equal($arg1 as xs:gYearMonth, $arg2 as xs:gYearMonth) as xs:boolean
op:gYear-equal($arg1 as xs:gYear, $arg2 as xs:gYear) as xs:boolean
op:gMonthDay-equal($arg1 as xs:gMonthDay, $arg2 as xs:gMonthDay) as xs:boolean
op:gMonth-equal($arg1 as xs:gMonth, $arg2 as xs:gMonth) as xs:boolean
op:gDay-equal($arg1 as xs:gDay, $arg2 as xs:gDay) as xs:boolean
10.5 Component Extraction Functions on Durations, Dates and Times
fn:years-from-duration($arg as xs:duration?) as xs:integer?
fn:months-from-duration($arg as xs:duration?) as xs:integer?
fn:days-from-duration($arg as xs:duration?) as xs:integer?
fn:hours-from-duration($arg as xs:duration?) as xs:integer?
fn:minutes-from-duration($arg as xs:duration?) as xs:integer?
fn:seconds-from-duration($arg as xs:duration?) as xs:decimal?
fn:year-from-dateTime($arg as xs:dateTime?) as xs:integer?
fn:month-from-dateTime($arg as xs:dateTime?) as xs:integer?
fn:day-from-dateTime($arg as xs:dateTime?) as xs:integer?
fn:hours-from-dateTime($arg as xs:dateTime?) as xs:integer?
fn:minutes-from-dateTime($arg as xs:dateTime?) as xs:integer?
fn:seconds-from-dateTime($arg as xs:dateTime?) as xs:decimal?
fn:timezone-from-dateTime($arg as xs:dateTime?) as xs:dayTimeDuration?
fn:year-from-date($arg as xs:date?) as xs:integer?
fn:month-from-date($arg as xs:date?) as xs:integer?
fn:day-from-date($arg as xs:date?) as xs:integer?
fn:timezone-from-date($arg as xs:date?) as xs:dayTimeDuration?
fn:hours-from-time($arg as xs:time?) as xs:integer?
fn:minutes-from-time($arg as xs:time?) as xs:integer?
fn:seconds-from-time($arg as xs:time?) as xs:decimal?
fn:timezone-from-time($arg as xs:time?) as xs:dayTimeDuration?
10.6 Arithmetic Operators on Durations
op:add-yearMonthDurations($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:yearMonthDuration
op:subtract-yearMonthDurations($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:yearMonthDuration
op:multiply-yearMonthDuration($arg1 as xs:yearMonthDuration, $arg2 as xs:double) as xs:yearMonthDuration
op:divide-yearMonthDuration($arg1 as xs:yearMonthDuration, $arg2 as xs:double) as xs:yearMonthDuration
op:divide-yearMonthDuration-by-yearMonthDuration($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:decimal
op:add-dayTimeDurations($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:dayTimeDuration
op:subtract-dayTimeDurations($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:dayTimeDuration
op:multiply-dayTimeDuration($arg1 as xs:dayTimeDuration, $arg2 as xs:double) as xs:dayTimeDuration
op:divide-dayTimeDuration($arg1 as xs:dayTimeDuration, $arg2 as xs:double) as xs:dayTimeDuration
op:divide-dayTimeDuration-by-dayTimeDuration($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:decimal
10.7 Timezone Adjustment Functions on Dates and Time Values
fn:adjust-dateTime-to-timezone($arg as xs:dateTime?) as xs:dateTime?
fn:adjust-dateTime-to-timezone($arg as xs:dateTime?, $timezone as xs:dayTimeDuration?) as xs:dateTime?
fn:adjust-date-to-timezone($arg as xs:date?) as xs:date?
fn:adjust-date-to-timezone($arg as xs:date?, $timezone as xs:dayTimeDuration?) as xs:date?
fn:adjust-time-to-timezone($arg as xs:time?) as xs:time?
fn:adjust-time-to-timezone($arg as xs:time?, $timezone as xs:dayTimeDuration?) as xs:time?
10.8 Arithmetic Operators on Durations, Dates and Times
op:subtract-dateTimes($arg1 as xs:dateTime, $arg2 as xs:dateTime) as xs:dayTimeDuration
op:subtract-dates($arg1 as xs:date, $arg2 as xs:date) as xs:dayTimeDuration
op:subtract-times($arg1 as xs:time, $arg2 as xs:time) as xs:dayTimeDuration
op:add-yearMonthDuration-to-dateTime($arg1 as xs:dateTime, $arg2 as xs:yearMonthDuration) as xs:dateTime
op:add-dayTimeDuration-to-dateTime($arg1 as xs:dateTime, $arg2 as xs:dayTimeDuration) as xs:dateTime
op:subtract-yearMonthDuration-from-dateTime($arg1 as xs:dateTime, $arg2 as xs:yearMonthDuration) as xs:dateTime
op:subtract-dayTimeDuration-from-dateTime($arg1 as xs:dateTime, $arg2 as xs:dayTimeDuration) as xs:dateTime
op:add-yearMonthDuration-to-date($arg1 as xs:date, $arg2 as xs:yearMonthDuration) as xs:date
op:add-dayTimeDuration-to-date($arg1 as xs:date, $arg2 as xs:dayTimeDuration) as xs:date
op:subtract-yearMonthDuration-from-date($arg1 as xs:date, $arg2 as xs:yearMonthDuration) as xs:date
op:subtract-dayTimeDuration-from-date($arg1 as xs:date, $arg2 as xs:dayTimeDuration) as xs:date
op:add-dayTimeDuration-to-time($arg1 as xs:time, $arg2 as xs:dayTimeDuration) as xs:time
op:subtract-dayTimeDuration-from-time($arg1 as xs:time, $arg2 as xs:dayTimeDuration) as xs:time
11 Functions Related to QNames
11.1 Additional Constructor Functions for QNames
fn:resolve-QName($qname as xs:string?, $element as element()) as xs:QName?
fn:QName($paramURI as xs:string?, $paramQName as xs:string) as xs:QName
11.2 Functions and Operators Related to QNames
op:QName-equal($arg1 as xs:QName, $arg2 as xs:QName) as xs:boolean
fn:prefix-from-QName($arg as xs:QName?) as xs:NCName?
fn:local-name-from-QName($arg as xs:QName?) as xs:NCName?
fn:namespace-uri-from-QName($arg as xs:QName?) as xs:anyURI?
fn:namespace-uri-for-prefix($prefix as xs:string?, $element as element()) as xs:anyURI?
fn:in-scope-prefixes($element as element()) as xs:string*
12 Operators on base64Binary and hexBinary
12.1 Comparisons of base64Binary and hexBinary Values
op:hexBinary-equal($value1 as xs:hexBinary, $value2 as xs:hexBinary) as xs:boolean
op:base64Binary-equal($value1 as xs:base64Binary, $value2 as xs:base64Binary) as xs:boolean
13 Operators on NOTATION
13.1 Operators on NOTATION
op:NOTATION-equal($arg1 as xs:NOTATION, $arg2 as xs:NOTATION) as xs:boolean
14 Functions and Operators on Nodes
14.1 fn:name
fn:name() as xs:string
fn:name($arg as node()?) as xs:string
14.2 fn:local-name
fn:local-name() as xs:string
fn:local-name($arg as node()?) as xs:string
14.3 fn:namespace-uri
fn:namespace-uri() as xs:anyURI
fn:namespace-uri($arg as node()?) as xs:anyURI
14.4 fn:number
fn:number() as xs:double
fn:number($arg as xs:anyAtomicType?) as xs:double
14.5 fn:lang
fn:lang($testlang as xs:string?) as xs:boolean
fn:lang($testlang as xs:string?, $node as node()) as xs:boolean
14.6 op:is-same-node
op:is-same-node($parameter1 as node(), $parameter2 as node()) as xs:boolean
14.7 op:node-before
op:node-before($parameter1 as node(), $parameter2 as node()) as xs:boolean
14.8 op:node-after
op:node-after($parameter1 as node(), $parameter2 as node()) as xs:boolean
14.9 fn:root
fn:root() as node()
fn:root($arg as node()?) as node()?
15 Functions and Operators on Sequences
15.1 General Functions and Operators on Sequences
fn:boolean($arg as item()*) as xs:boolean
op:concatenate($seq1 as item()*, $seq2 as item()*) as item()*
fn:index-of($seqParam as xs:anyAtomicType*, $srchParam as xs:anyAtomicType) as xs:integer*
fn:index-of($seqParam as xs:anyAtomicType*, $srchParam as xs:anyAtomicType, $collation as xs:string) as xs:integer*
fn:empty($arg as item()*) as xs:boolean
fn:exists($arg as item()*) as xs:boolean
fn:distinct-values($arg as xs:anyAtomicType*) as xs:anyAtomicType*
fn:distinct-values($arg as xs:anyAtomicType*, $collation as xs:string) as xs:anyAtomicType*
fn:insert-before($target as item()*, $position as xs:integer, $inserts as item()*) as item()*
fn:remove($target as item()*, $position as xs:integer) as item()*
fn:reverse($arg as item()*) as item()*
fn:subsequence($sourceSeq as item()*, $startingLoc as xs:double) as item()*
fn:subsequence($sourceSeq as item()*, $startingLoc as xs:double, $length as xs:double) as item()*
fn:unordered($sourceSeq as item()*) as item()*
15.2 Functions That Test the Cardinality of Sequences
fn:zero-or-one($arg as item()*) as item()?
fn:one-or-more($arg as item()*) as item()+
fn:exactly-one($arg as item()*) as item()
15.3 Equals, Union, Intersection and Except
fn:deep-equal($parameter1 as item()*, $parameter2 as item()*) as xs:boolean
fn:deep-equal($parameter1 as item()*, $parameter2 as item()*, $collation as string) as xs:boolean
op:union($parameter1 as node()*, $parameter2 as node()*) as node()*
op:intersect($parameter1 as node()*, $parameter2 as node()*) as node()*
op:except($parameter1 as node()*, $parameter2 as node()*) as node()*
15.4 Aggregate Functions
fn:count($arg as item()*) as xs:integer
fn:avg($arg as xs:anyAtomicType*) as xs:anyAtomicType?
fn:max($arg as xs:anyAtomicType*) as xs:anyAtomicType?
fn:max($arg as xs:anyAtomicType*, $collation as string) as xs:anyAtomicType?
fn:min($arg as xs:anyAtomicType*) as xs:anyAtomicType?
fn:min($arg as xs:anyAtomicType*, $collation as string) as xs:anyAtomicType?
fn:sum($arg as xs:anyAtomicType*) as xs:anyAtomicType
fn:sum($arg as xs:anyAtomicType*, $zero as xs:anyAtomicType?) as xs:anyAtomicType?
15.5 Functions and Operators that Generate Sequences
op:to($firstval as xs:integer, $lastval as xs:integer) as xs:integer*
fn:id($arg as xs:string*) as element()*
fn:id($arg as xs:string*, $node as node()) as element()*
fn:idref($arg as xs:string*) as node()*
fn:idref($arg as xs:string*, $node as node()) as node()*
fn:doc($uri as xs:string?) as document-node()?
fn:doc-available($uri as xs:string?) as xs:boolean
fn:collection() as node()*
fn:collection($arg as xs:string?) as node()*
fn:element-with-id($arg as xs:string*) as element()*
fn:element-with-id($arg as xs:string*, $node as node()) as element()*
16 Context Functions
16.1 fn:position
fn:position() as xs:integer
16.2 fn:last
fn:last() as xs:integer
16.3 fn:current-dateTime
fn:current-dateTime() as xs:dateTime
16.4 fn:current-date
fn:current-date() as xs:date
16.5 fn:current-time
fn:current-time() as xs:time
16.6 fn:implicit-timezone
fn:implicit-timezone() as xs:dayTimeDuration
16.7 fn:default-collation
fn:default-collation() as xs:string
16.8 fn:static-base-uri
fn:static-base-uri() as xs:anyURI?

----------

op:NOTATION-equal($arg1 as xs:NOTATION, $arg2 as xs:NOTATION) as xs:boolean (§13.1.1)
fn:QName($paramURI as xs:string?, $paramQName as xs:string) as xs:QName (§11.1.2)
op:QName-equal($arg1 as xs:QName, $arg2 as xs:QName) as xs:boolean (§11.2.1)
fn:abs($arg as numeric?) as numeric? (§6.4.1)
op:add-dayTimeDuration-to-date($arg1 as xs:date, $arg2 as xs:dayTimeDuration) as xs:date (§10.8.9)
op:add-dayTimeDuration-to-dateTime($arg1 as xs:dateTime, $arg2 as xs:dayTimeDuration) as xs:dateTime (§10.8.5)
op:add-dayTimeDuration-to-time($arg1 as xs:time, $arg2 as xs:dayTimeDuration) as xs:time (§10.8.12)
op:add-dayTimeDurations($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:dayTimeDuration (§10.6.6)
op:add-yearMonthDuration-to-date($arg1 as xs:date, $arg2 as xs:yearMonthDuration) as xs:date (§10.8.8)
op:add-yearMonthDuration-to-dateTime($arg1 as xs:dateTime, $arg2 as xs:yearMonthDuration) as xs:dateTime (§10.8.4)
op:add-yearMonthDurations($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:yearMonthDuration (§10.6.1)
fn:adjust-date-to-timezone($arg as xs:date?) as xs:date? (§10.7.2)
fn:adjust-date-to-timezone($arg as xs:date?, $timezone as xs:dayTimeDuration?) as xs:date? (§10.7.2)
fn:adjust-dateTime-to-timezone($arg as xs:dateTime?) as xs:dateTime? (§10.7.1)
fn:adjust-dateTime-to-timezone($arg as xs:dateTime?, $timezone as xs:dayTimeDuration?) as xs:dateTime? (§10.7.1)
fn:adjust-time-to-timezone($arg as xs:time?) as xs:time? (§10.7.3)
fn:adjust-time-to-timezone($arg as xs:time?, $timezone as xs:dayTimeDuration?) as xs:time? (§10.7.3)
fn:avg($arg as xs:anyAtomicType*) as xs:anyAtomicType? (§15.4.2)
fn:base-uri() as xs:anyURI? (§2.5)
fn:base-uri($arg as node()?) as xs:anyURI? (§2.5)
op:base64Binary-equal($value1 as xs:base64Binary, $value2 as xs:base64Binary) as xs:boolean (§12.1.2)
fn:boolean($arg as item()*) as xs:boolean (§15.1.1)
op:boolean-equal($value1 as xs:boolean, $value2 as xs:boolean) as xs:boolean (§9.2.1)
op:boolean-greater-than($arg1 as xs:boolean, $arg2 as xs:boolean) as xs:boolean (§9.2.3)
op:boolean-less-than($arg1 as xs:boolean, $arg2 as xs:boolean) as xs:boolean (§9.2.2)
fn:ceiling($arg as numeric?) as numeric? (§6.4.2)
fn:codepoint-equal($comparand1 as xs:string?, $comparand2 as xs:string?) as xs:boolean? (§7.3.3)
fn:codepoints-to-string($arg as xs:integer*) as xs:string (§7.2.1)
fn:collection() as node()* (§15.5.6)
fn:collection($arg as xs:string?) as node()* (§15.5.6)
fn:compare($comparand1 as xs:string?, $comparand2 as xs:string?) as xs:integer? (§7.3.2)
fn:compare($comparand1 as xs:string?, $comparand2 as xs:string?, $collation as xs:string) as xs:integer? (§7.3.2)
fn:concat($arg1 as xs:anyAtomicType?, $arg2 as xs:anyAtomicType?, ...) as xs:string (§7.4.1)
op:concatenate($seq1 as item()*, $seq2 as item()*) as item()* (§15.1.2)
fn:contains($arg1 as xs:string?, $arg2 as xs:string?) as xs:boolean (§7.5.1)
fn:contains($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:boolean (§7.5.1)
fn:count($arg as item()*) as xs:integer (§15.4.1)
fn:current-date() as xs:date (§16.4)
fn:current-dateTime() as xs:dateTime (§16.3)
fn:current-time() as xs:time (§16.5)
fn:data($arg as item()*) as xs:anyAtomicType* (§2.4)
op:date-equal($arg1 as xs:date, $arg2 as xs:date) as xs:boolean (§10.4.9)
op:date-greater-than($arg1 as xs:date, $arg2 as xs:date) as xs:boolean (§10.4.11)
op:date-less-than($arg1 as xs:date, $arg2 as xs:date) as xs:boolean (§10.4.10)
fn:dateTime($arg1 as xs:date?, $arg2 as xs:time?) as xs:dateTime? (§5.2)
op:dateTime-equal($arg1 as xs:dateTime, $arg2 as xs:dateTime) as xs:boolean (§10.4.6)
op:dateTime-greater-than($arg1 as xs:dateTime, $arg2 as xs:dateTime) as xs:boolean (§10.4.8)
op:dateTime-less-than($arg1 as xs:dateTime, $arg2 as xs:dateTime) as xs:boolean (§10.4.7)
fn:day-from-date($arg as xs:date?) as xs:integer? (§10.5.16)
fn:day-from-dateTime($arg as xs:dateTime?) as xs:integer? (§10.5.9)
op:dayTimeDuration-greater-than($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:boolean (§10.4.4)
op:dayTimeDuration-less-than($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:boolean (§10.4.3)
fn:days-from-duration($arg as xs:duration?) as xs:integer? (§10.5.3)
fn:deep-equal($parameter1 as item()*, $parameter2 as item()*) as xs:boolean (§15.3.1)
fn:deep-equal($parameter1 as item()*, $parameter2 as item()*, $collation as string) as xs:boolean (§15.3.1)
fn:default-collation() as xs:string (§16.7)
fn:distinct-values($arg as xs:anyAtomicType*) as xs:anyAtomicType* (§15.1.6)
fn:distinct-values($arg as xs:anyAtomicType*, $collation as xs:string) as xs:anyAtomicType* (§15.1.6)
op:divide-dayTimeDuration($arg1 as xs:dayTimeDuration, $arg2 as xs:double) as xs:dayTimeDuration (§10.6.9)
op:divide-dayTimeDuration-by-dayTimeDuration($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:decimal (§10.6.10)
op:divide-yearMonthDuration($arg1 as xs:yearMonthDuration, $arg2 as xs:double) as xs:yearMonthDuration (§10.6.4)
op:divide-yearMonthDuration-by-yearMonthDuration($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:decimal (§10.6.5)
fn:doc($uri as xs:string?) as document-node()? (§15.5.4)
fn:doc-available($uri as xs:string?) as xs:boolean (§15.5.5)
fn:document-uri($arg as node()?) as xs:anyURI? (§2.6)
op:duration-equal($arg1 as xs:duration, $arg2 as xs:duration) as xs:boolean (§10.4.5)
fn:element-with-id($arg as xs:string*) as element()* (§15.5.7)
fn:element-with-id($arg as xs:string*, $node as node()) as element()* (§15.5.7)
fn:empty($arg as item()*) as xs:boolean (§15.1.4)
fn:encode-for-uri($uri-part as xs:string?) as xs:string (§7.4.10)
fn:ends-with($arg1 as xs:string?, $arg2 as xs:string?) as xs:boolean (§7.5.3)
fn:ends-with($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:boolean (§7.5.3)
fn:error() as none (§3)
fn:error($error as xs:QName) as none (§3)
fn:error($error as xs:QName?, $description as xs:string) as none (§3)
fn:error($error as xs:QName?, $description as xs:string, $error-object as item()*) as none (§3)
fn:escape-html-uri($uri as xs:string?) as xs:string (§7.4.12)
fn:exactly-one($arg as item()*) as item() (§15.2.3)
op:except($parameter1 as node()*, $parameter2 as node()*) as node()* (§15.3.4)
fn:exists($arg as item()*) as xs:boolean (§15.1.5)
fn:false() as xs:boolean (§9.1.2)
fn:floor($arg as numeric?) as numeric? (§6.4.3)
op:gDay-equal($arg1 as xs:gDay, $arg2 as xs:gDay) as xs:boolean (§10.4.19)
op:gMonth-equal($arg1 as xs:gMonth, $arg2 as xs:gMonth) as xs:boolean (§10.4.18)
op:gMonthDay-equal($arg1 as xs:gMonthDay, $arg2 as xs:gMonthDay) as xs:boolean (§10.4.17)
op:gYear-equal($arg1 as xs:gYear, $arg2 as xs:gYear) as xs:boolean (§10.4.16)
op:gYearMonth-equal($arg1 as xs:gYearMonth, $arg2 as xs:gYearMonth) as xs:boolean (§10.4.15)
op:hexBinary-equal($value1 as xs:hexBinary, $value2 as xs:hexBinary) as xs:boolean (§12.1.1)
fn:hours-from-dateTime($arg as xs:dateTime?) as xs:integer? (§10.5.10)
fn:hours-from-duration($arg as xs:duration?) as xs:integer? (§10.5.4)
fn:hours-from-time($arg as xs:time?) as xs:integer? (§10.5.18)
fn:id($arg as xs:string*) as element()* (§15.5.2)
fn:id($arg as xs:string*, $node as node()) as element()* (§15.5.2)
fn:idref($arg as xs:string*) as node()* (§15.5.3)
fn:idref($arg as xs:string*, $node as node()) as node()* (§15.5.3)
fn:implicit-timezone() as xs:dayTimeDuration (§16.6)
fn:in-scope-prefixes($element as element()) as xs:string* (§11.2.6)
fn:index-of($seqParam as xs:anyAtomicType*, $srchParam as xs:anyAtomicType) as xs:integer* (§15.1.3)
fn:index-of($seqParam as xs:anyAtomicType*, $srchParam as xs:anyAtomicType, $collation as xs:string) as xs:integer* (§15.1.3)
fn:insert-before($target as item()*, $position as xs:integer, $inserts as item()*) as item()* (§15.1.7)
op:intersect($parameter1 as node()*, $parameter2 as node()*) as node()* (§15.3.3)
fn:iri-to-uri($iri as xs:string?) as xs:string (§7.4.11)
op:is-same-node($parameter1 as node(), $parameter2 as node()) as xs:boolean (§14.6)
fn:lang($testlang as xs:string?) as xs:boolean (§14.5)
fn:lang($testlang as xs:string?, $node as node()) as xs:boolean (§14.5)
fn:last() as xs:integer (§16.2)
fn:local-name() as xs:string (§14.2)
fn:local-name($arg as node()?) as xs:string (§14.2)
fn:local-name-from-QName($arg as xs:QName?) as xs:NCName? (§11.2.3)
fn:lower-case($arg as xs:string?) as xs:string (§7.4.8)
fn:matches($input as xs:string?, $pattern as xs:string) as xs:boolean (§7.6.2)
fn:matches($input as xs:string?, $pattern as xs:string, $flags as xs:string) as xs:boolean (§7.6.2)
fn:max($arg as xs:anyAtomicType*) as xs:anyAtomicType? (§15.4.3)
fn:max($arg as xs:anyAtomicType*, $collation as string) as xs:anyAtomicType? (§15.4.3)
fn:min($arg as xs:anyAtomicType*) as xs:anyAtomicType? (§15.4.4)
fn:min($arg as xs:anyAtomicType*, $collation as string) as xs:anyAtomicType? (§15.4.4)
fn:minutes-from-dateTime($arg as xs:dateTime?) as xs:integer? (§10.5.11)
fn:minutes-from-duration($arg as xs:duration?) as xs:integer? (§10.5.5)
fn:minutes-from-time($arg as xs:time?) as xs:integer? (§10.5.19)
fn:month-from-date($arg as xs:date?) as xs:integer? (§10.5.15)
fn:month-from-dateTime($arg as xs:dateTime?) as xs:integer? (§10.5.8)
fn:months-from-duration($arg as xs:duration?) as xs:integer? (§10.5.2)
op:multiply-dayTimeDuration($arg1 as xs:dayTimeDuration, $arg2 as xs:double) as xs:dayTimeDuration (§10.6.8)
op:multiply-yearMonthDuration($arg1 as xs:yearMonthDuration, $arg2 as xs:double) as xs:yearMonthDuration (§10.6.3)
fn:name() as xs:string (§14.1)
fn:name($arg as node()?) as xs:string (§14.1)
fn:namespace-uri() as xs:anyURI (§14.3)
fn:namespace-uri($arg as node()?) as xs:anyURI (§14.3)
fn:namespace-uri-for-prefix($prefix as xs:string?, $element as element()) as xs:anyURI? (§11.2.5)
fn:namespace-uri-from-QName($arg as xs:QName?) as xs:anyURI? (§11.2.4)
fn:nilled($arg as node()?) as xs:boolean? (§2.2)
op:node-after($parameter1 as node(), $parameter2 as node()) as xs:boolean (§14.8)
op:node-before($parameter1 as node(), $parameter2 as node()) as xs:boolean (§14.7)
fn:node-name($arg as node()?) as xs:QName? (§2.1)
fn:normalize-space() as xs:string (§7.4.5)
fn:normalize-space($arg as xs:string?) as xs:string (§7.4.5)
fn:normalize-unicode($arg as xs:string?) as xs:string (§7.4.6)
fn:normalize-unicode($arg as xs:string?, $normalizationForm as xs:string) as xs:string (§7.4.6)
fn:not($arg as item()*) as xs:boolean (§9.3.1)
fn:number() as xs:double (§14.4)
fn:number($arg as xs:anyAtomicType?) as xs:double (§14.4)
op:numeric-add($arg1 as numeric, $arg2 as numeric) as numeric (§6.2.1)
op:numeric-divide($arg1 as numeric, $arg2 as numeric) as numeric (§6.2.4)
op:numeric-equal($arg1 as numeric, $arg2 as numeric) as xs:boolean (§6.3.1)
op:numeric-greater-than($arg1 as numeric, $arg2 as numeric) as xs:boolean (§6.3.3)
op:numeric-integer-divide($arg1 as numeric, $arg2 as numeric) as xs:integer (§6.2.5)
op:numeric-less-than($arg1 as numeric, $arg2 as numeric) as xs:boolean (§6.3.2)
op:numeric-mod($arg1 as numeric, $arg2 as numeric) as numeric (§6.2.6)
op:numeric-multiply($arg1 as numeric, $arg2 as numeric) as numeric (§6.2.3)
op:numeric-subtract($arg1 as numeric, $arg2 as numeric) as numeric (§6.2.2)
op:numeric-unary-minus($arg as numeric) as numeric (§6.2.8)
op:numeric-unary-plus($arg as numeric) as numeric (§6.2.7)
fn:one-or-more($arg as item()*) as item()+ (§15.2.2)
fn:position() as xs:integer (§16.1)
fn:prefix-from-QName($arg as xs:QName?) as xs:NCName? (§11.2.2)
fn:remove($target as item()*, $position as xs:integer) as item()* (§15.1.8)
fn:replace($input as xs:string?, $pattern as xs:string, $replacement as xs:string) as xs:string (§7.6.3)
fn:replace($input as xs:string?, $pattern as xs:string, $replacement as xs:string, $flags as xs:string) as xs:string (§7.6.3)
fn:resolve-QName($qname as xs:string?, $element as element()) as xs:QName? (§11.1.1)
fn:resolve-uri($relative as xs:string?) as xs:anyURI? (§8.1)
fn:resolve-uri($relative as xs:string?, $base as xs:string) as xs:anyURI? (§8.1)
fn:reverse($arg as item()*) as item()* (§15.1.9)
fn:root() as node() (§14.9)
fn:root($arg as node()?) as node()? (§14.9)
fn:round($arg as numeric?) as numeric? (§6.4.4)
fn:round-half-to-even($arg as numeric?) as numeric? (§6.4.5)
fn:round-half-to-even($arg as numeric?, $precision as xs:integer) as numeric? (§6.4.5)
fn:seconds-from-dateTime($arg as xs:dateTime?) as xs:decimal? (§10.5.12)
fn:seconds-from-duration($arg as xs:duration?) as xs:decimal? (§10.5.6)
fn:seconds-from-time($arg as xs:time?) as xs:decimal? (§10.5.20)
fn:starts-with($arg1 as xs:string?, $arg2 as xs:string?) as xs:boolean (§7.5.2)
fn:starts-with($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:boolean (§7.5.2)
fn:static-base-uri() as xs:anyURI? (§16.8)
fn:string() as xs:string (§2.3)
fn:string($arg as item()?) as xs:string (§2.3)
fn:string-join($arg1 as xs:string*, $arg2 as xs:string) as xs:string (§7.4.2)
fn:string-length() as xs:integer (§7.4.4)
fn:string-length($arg as xs:string?) as xs:integer (§7.4.4)
fn:string-to-codepoints($arg as xs:string?) as xs:integer* (§7.2.2)
fn:subsequence($sourceSeq as item()*, $startingLoc as xs:double) as item()* (§15.1.10)
fn:subsequence($sourceSeq as item()*, $startingLoc as xs:double, $length as xs:double) as item()* (§15.1.10)
fn:substring($sourceString as xs:string?, $startingLoc as xs:double) as xs:string (§7.4.3)
fn:substring($sourceString as xs:string?, $startingLoc as xs:double, $length as xs:double) as xs:string (§7.4.3)
fn:substring-after($arg1 as xs:string?, $arg2 as xs:string?) as xs:string (§7.5.5)
fn:substring-after($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:string (§7.5.5)
fn:substring-before($arg1 as xs:string?, $arg2 as xs:string?) as xs:string (§7.5.4)
fn:substring-before($arg1 as xs:string?, $arg2 as xs:string?, $collation as xs:string) as xs:string (§7.5.4)
op:subtract-dateTimes($arg1 as xs:dateTime, $arg2 as xs:dateTime) as xs:dayTimeDuration (§10.8.1)
op:subtract-dates($arg1 as xs:date, $arg2 as xs:date) as xs:dayTimeDuration (§10.8.2)
op:subtract-dayTimeDuration-from-date($arg1 as xs:date, $arg2 as xs:dayTimeDuration) as xs:date (§10.8.11)
op:subtract-dayTimeDuration-from-dateTime($arg1 as xs:dateTime, $arg2 as xs:dayTimeDuration) as xs:dateTime (§10.8.7)
op:subtract-dayTimeDuration-from-time($arg1 as xs:time, $arg2 as xs:dayTimeDuration) as xs:time (§10.8.13)
op:subtract-dayTimeDurations($arg1 as xs:dayTimeDuration, $arg2 as xs:dayTimeDuration) as xs:dayTimeDuration (§10.6.7)
op:subtract-times($arg1 as xs:time, $arg2 as xs:time) as xs:dayTimeDuration (§10.8.3)
op:subtract-yearMonthDuration-from-date($arg1 as xs:date, $arg2 as xs:yearMonthDuration) as xs:date (§10.8.10)
op:subtract-yearMonthDuration-from-dateTime($arg1 as xs:dateTime, $arg2 as xs:yearMonthDuration) as xs:dateTime (§10.8.6)
op:subtract-yearMonthDurations($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:yearMonthDuration (§10.6.2)
fn:sum($arg as xs:anyAtomicType*) as xs:anyAtomicType (§15.4.5)
fn:sum($arg as xs:anyAtomicType*, $zero as xs:anyAtomicType?) as xs:anyAtomicType? (§15.4.5)
op:time-equal($arg1 as xs:time, $arg2 as xs:time) as xs:boolean (§10.4.12)
op:time-greater-than($arg1 as xs:time, $arg2 as xs:time) as xs:boolean (§10.4.14)
op:time-less-than($arg1 as xs:time, $arg2 as xs:time) as xs:boolean (§10.4.13)
fn:timezone-from-date($arg as xs:date?) as xs:dayTimeDuration? (§10.5.17)
fn:timezone-from-dateTime($arg as xs:dateTime?) as xs:dayTimeDuration? (§10.5.13)
fn:timezone-from-time($arg as xs:time?) as xs:dayTimeDuration? (§10.5.21)
op:to($firstval as xs:integer, $lastval as xs:integer) as xs:integer* (§15.5.1)
fn:tokenize($input as xs:string?, $pattern as xs:string) as xs:string* (§7.6.4)
fn:tokenize($input as xs:string?, $pattern as xs:string, $flags as xs:string) as xs:string* (§7.6.4)
fn:trace($value as item()*, $label as xs:string) as item()* (§4)
fn:translate($arg as xs:string?, $mapString as xs:string, $transString as xs:string) as xs:string (§7.4.9)
fn:true() as xs:boolean (§9.1.1)
op:union($parameter1 as node()*, $parameter2 as node()*) as node()* (§15.3.2)
fn:unordered($sourceSeq as item()*) as item()* (§15.1.11)
fn:upper-case($arg as xs:string?) as xs:string (§7.4.7)
fn:year-from-date($arg as xs:date?) as xs:integer? (§10.5.14)
fn:year-from-dateTime($arg as xs:dateTime?) as xs:integer? (§10.5.7)
op:yearMonthDuration-greater-than($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:boolean (§10.4.2)
op:yearMonthDuration-less-than($arg1 as xs:yearMonthDuration, $arg2 as xs:yearMonthDuration) as xs:boolean (§10.4.1)
fn:years-from-duration($arg as xs:duration?) as xs:integer? (§10.5.1)
fn:zero-or-one($arg as item()*) as item()? (§15.2.1)