add_rules("mode.debug")

set_languages("cxx11")
add_includedirs(".")

-- verify lib
add_includedirs("dstruct")

if d2x.private.d2ds_difficulty_level == 0 then
    includes("tests") -- + exeraries
elseif d2x.private.d2ds_difficulty_level == 1 then
    includes("useage")
    includes("tests") -- + exeraries
else
    includes("useage")
end