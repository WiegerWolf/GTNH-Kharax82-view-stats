from pytubefix import Playlist
import matplotlib.pyplot as plt
import pandas as pd

# Create playlist object
playlist_url = "https://www.youtube.com/playlist?list=PLliiJ70rl2NvJjby2LoVuP1EuOvRAyf97"
playlist = Playlist(playlist_url)

# Collect video data
videos = []
for video in playlist.videos:
    try:
        title = video.title
        views = video.views
        videos.append({
            'title': title,
            'views': views
        })
        print(f"Processed: {title}")
    except Exception as e:
        print(f"Error processing video: {e}")

# Create DataFrame
df = pd.DataFrame(videos)

# Create bar chart
plt.figure(figsize=(15, 8))
plt.bar(range(len(df)), df['views'])
plt.xticks(range(len(df)), df['title'], rotation=45, ha='right')
plt.title('Views per Episode')
plt.xlabel('Episode Title')
plt.ylabel('Views')
plt.tight_layout()
plt.show()

# Print the data
print("\nViews per episode:")
print(df.to_string(index=False))
