# pla[nt]cards

This branch, `plantcards`, is a tentative rewrite from Python to JS, motivated by wanting some simple nametags for my
houseplants. My hope is that rewriting this tool in a language I'm more facile with will make it easier to generalize
for multiple templates and data sources.

## Imagined workflow

1. Export CSV from Google Sheet of plants
1. Run `generate` to convert CSV &rarr; JSON &rarr; HTML
