"""
TODO: Write a function "filterSongs" that loops through passed in albums and
      their songs, applies various filters, and returns a list of songs that
      pass all the applied filters:
    * Function should take in a parameter "albums", whose value is a list of
      Album objects
        - There needs to be at least 1 Album in the "albums" list parameter
    * Function should take in a parameter "name", that is used to filter based
      on the name of a song.
        - Should the value of "name" be None, the filter will not be applied
        - Should the value of "name" be a str, the filter will be passed if
          the value, case insensitive, of "name" is present in the song's name
    * Function should take in a parameter "minDuration", that is used to filter
      based on the duration of a song.
        - Should the value of "minDuration" be None, the filter will not be
          applied
        - Should the value of "minDuration" be an int, the filter will be
          passed if the value of "minduration" is less than or equal to the
          song's duration
    * Function should take in a parameter "maxDuration", that is used to filter
      based on the duration of a song.
        - Should the value of "maxDuration" be None, the filter will not be
          applied
        - Should the value of "maxDuration" be an int, the filter will be
          passed if the value of "maxDuration" is greater than or equal to the
          song's duration
    * Function should take in a parameter "minReleaseDate", that is used to
      filter based on the release_date of a song.
        - Should the value of "minReleaseDate" be None, the filter will not be
          applied
        - Should the value of "minReleaseDate" be an int, the filter will be
          passed if the value of "minReleaseDate" is less than or equal to the
          song's release_date
    * Function should take in a parameter "maxReleaseDate", that is used to
      filter
      based on the duration of a song.
        - Should the value of "maxReleaseDate" be None, the filter will not be
          applied
        - Should the value of "maxReleaseDate" be an int, the filter will be
          passed if the value of "maxReleaseDate" is greater than or equal to
          the song's release_date
    * Function should return a list of Song objects that pass all the filters
      applied
        - Should no songs pass all applied filters, an empty list should be
          returned
"""