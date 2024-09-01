import whisper
import os
from tqdm import tqdm
whisper_model = None


def load_whisper(model="large"):
    global whisper_model
    whisper_model = whisper.load_model(model, device="cuda")
    print("Whisper模型："+model)

def run_analysis(title, filename, model="tiny", prompt="以下是普通话的句子。"):
    global whisper_model
    # print("正在加载Whisper模型...")
    # 读取列表中的音频文件
    audio_list = os.listdir(f"audio/slice/{filename}")
    # print("加载Whisper模型成功！")
    # 创建outputs文件夹
    os.makedirs("outputs", exist_ok=True)
    print("正在转换文本...")

    for i in range(1, len(audio_list)+1):
        print(f"正在转换第{i}/{len(audio_list)}个音频")
        # 识别音频
        result = whisper_model.transcribe(f"audio/slice/{filename}/{i}.mp3", initial_prompt=prompt)
        print("".join([i["text"] for i in result["segments"] if i is not None]))

        with open(f"outputs/{title}.txt", "a", encoding="utf-8") as f:
            f.write("".join([i["text"] for i in result["segments"] if i is not None]))
            f.write("\n")
        i += 1

    # i = 1
    # for fn in audio_list:
    #     print(f"正在转换第{i}/{len(audio_list)}个音频... {fn}")
    #     # 识别音频
    #     result = whisper_model.transcribe(f"audio/slice/{filename}/{fn}", initial_prompt=prompt)
    #     print("".join([i["text"] for i in result["segments"] if i is not None]))

    #     with open(f"outputs/{filename}.txt", "a", encoding="utf-8") as f:
    #         f.write("".join([i["text"] for i in result["segments"] if i is not None]))
    #         f.write("\n")
    #     i += 1
    

# run_analysis("20231125133459")