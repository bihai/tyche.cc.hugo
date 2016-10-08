---
date: 2015-11-25T23:10:39+01:00
doc:
- commands_en
slug: hugo
title: hugo
url: /doc/commands/hugo_en
---

## hugo

hugo builds your site

### Synopsis


hugo is the main command, used to build your Hugo site.

Hugo is a Fast and Flexible Static Site Generator
built with love by spf13 and friends in Go.

Complete documentation is available at http://gohugo.io/.

```
hugo
```

### Options

```
  -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
  -D, --buildDrafts[=false]: include content marked as draft
  -F, --buildFuture[=false]: include content with publishdate in the future
      --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
      --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
      --config="": config file (default is path/config.yaml|json|toml)
  -d, --destination="": filesystem path to write files to
      --disableRSS[=false]: Do not build RSS files
      --disableSitemap[=false]: Do not build Sitemap file
      --editor="": edit new content with this editor, if provided
      --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
      --log[=false]: Enable Logging
      --logFile="": Log File path (if set, logging enabled automatically)
      --noTimes[=false]: Don't sync modification time of files
      --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
      --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
  -s, --source="": filesystem path to read files relative from
      --stepAnalysis[=false]: display memory and timing of different steps of the program
  -t, --theme="": theme to use (located in /doc/themes/THEMENAME/)
      --uglyURLs[=false]: if true, use /filename.html instead of /filename/
  -v, --verbose[=false]: verbose output
      --verboseLog[=false]: verbose logging
  -w, --watch[=false]: watch filesystem for changes and recreate as needed
```

### SEE ALSO
* [hugo benchmark](/doc/commands/hugo_benchmark/)	 - Benchmark hugo by building a site a number of times.
* [hugo check](/doc/commands/hugo_check/)	 - Check content in the source directory
* [hugo config](/doc/commands/hugo_config/)	 - Print the site configuration
* [hugo convert](/doc/commands/hugo_convert/)	 - Convert your content to different formats
* [hugo gen](/doc/commands/hugo_gen/)	 - A collection of several useful generators.
* [hugo import](/doc/commands/hugo_import/)	 - Import your site from others.
* [hugo list](/doc/commands/hugo_list/)	 - Listing out various types of content
* [hugo new](/doc/commands/hugo_new/)	 - Create new content for your site
* [hugo server](/doc/commands/hugo_server/)	 - A high performance webserver
* [hugo undraft](/doc/commands/hugo_undraft/)	 - Undraft changes the content's draft status from 'True' to 'False'
* [hugo version](/doc/commands/hugo_version/)	 - Print the version number of Hugo

###### Auto generated by spf13/cobra on 25-Nov-2015