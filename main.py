import asyncio
import os
import edge_tts
from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips, concatenate_audioclips

VIDEO_INPUT = "hattervidi.mp4"
FINAL_OUTPUT = "kesz_video.mp4"
TEXT_FILE = "szoveg.txt"
VOICE = "en-US-ChristopherNeural"
TEMP_DIR = "temp_audio_chunks"

def load_lines():
    if not os.path.exists(TEXT_FILE):
        raise FileNotFoundError(f"Nem találom a {TEXT_FILE} fájlt!")
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        # Beolvassuk a sorokat, és kiszűrjük az üreseket
        return [line.strip() for line in f.read().split('\n') if line.strip()]

async def generate_audio_chunk(text, filename):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)

async def build_video():
    print("1. Szöveg beolvasása.")
    lines = load_lines()
    
    sentences = []
    current_sentence_lines = []
    for line in lines:
        current_sentence_lines.append(line)
        if line.endswith('.') or line.endswith('!') or line.endswith('?'):
            sentences.append(current_sentence_lines)
            current_sentence_lines = []
            
    if current_sentence_lines:
        sentences.append(current_sentence_lines)

    os.makedirs(TEMP_DIR, exist_ok=True)
    audio_clips = []
    subtitle_clips = []
    current_time = 0
    
    print("2.Hang generálása és mikroszinkronizálás")
    base_video = VideoFileClip(VIDEO_INPUT)
    
    for i, sentence_lines in enumerate(sentences):
        full_sentence_text = " ".join(sentence_lines)
        temp_filename = os.path.join(TEMP_DIR, f"sent_{i}.mp3")
        
        await generate_audio_chunk(full_sentence_text, temp_filename)
        sent_audio = AudioFileClip(temp_filename)
        audio_clips.append(sent_audio)
        total_chars = sum(len(l) for l in sentence_lines)
        
        for line in sentence_lines:
            line_weight = len(line) / total_chars
            line_duration = sent_audio.duration * line_weight
            
            txt_clip = TextClip(
                font="Arial", 
                text=line, 
                font_size=42, 
                color='white', 
                stroke_color='black', 
                stroke_width=2,
                size=(base_video.w - 100, 80),
                method='caption'
            )
            
            txt_clip = txt_clip.with_position(('center', base_video.h - 260)) \
                               .with_start(current_time) \
                               .with_duration(line_duration)
                               
            subtitle_clips.append(txt_clip)
            current_time += line_duration

    print("3. Összefűzés")
    final_audio = concatenate_audioclips(audio_clips)
    
    loops_needed = int(final_audio.duration // base_video.duration) + 1
    long_video = concatenate_videoclips([base_video] * loops_needed)
    video_clip = long_video.subclipped(0, final_audio.duration)
    
    final_video = CompositeVideoClip([video_clip] + subtitle_clips)
    final_video = final_video.with_audio(final_audio)
    
    print("Renderelés")
    final_video.write_videofile(FINAL_OUTPUT, fps=30, codec="libx264", audio_codec="aac")
    
    print("Tisztítás")
    for i in range(len(sentences)):
        try:
            os.remove(os.path.join(TEMP_DIR, f"sent_{i}.mp3"))
        except:
            pass
    try:
        os.rmdir(TEMP_DIR)
    except:
        pass

if __name__ == "__main__":
    asyncio.run(build_video())
    print("Kész!")
    
