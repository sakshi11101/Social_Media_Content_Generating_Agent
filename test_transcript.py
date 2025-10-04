from example import get_transcript

def main():
    video_id = 'OZ5OZZZ2cvk'
    print(f"Retrieving transcript for {video_id} in test...")
    try:
        transcript = get_transcript(video_id)
        print(f"Successfully retrieved transcript for {video_id}")
        print(f"Transcript length: {len(transcript)} characters")
        print(f"First 500 characters of transcript: {transcript[:500]}")
    except Exception as e:
        print(f"Failed to retrieve transcript for {video_id}: {e}")

if __name__ == "__main__":
    main()

