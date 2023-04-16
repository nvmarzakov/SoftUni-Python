def movie_organizer(*collection):
    organizer = {}
    final_result = []
    for current in collection:

        movie = current[0]
        genre = current[1]
        if genre not in organizer:
            organizer[genre] = []
        organizer[genre].append(movie)

    sorted_organizer_by_genre = sorted(organizer.items(), key=lambda x: (-len(x[1]), x[0]))
    for g, m in sorted_organizer_by_genre:
        final_result.append(f"{g} - {len(m)}")
        if m:
            final_result.extend({'\n'.join(("* " + i) for i in sorted(m))})
    return "\n".join(final_result)
    
    print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
