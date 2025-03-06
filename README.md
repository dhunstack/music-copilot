# Music Copilot 🎵

A Streamlit-based web application for generating and visualizing Irish music using AI. This project combines music generation using transformers via natural language prompts, sheet music editing via abc notation, and audio playback capabilities.

Demo Video
[![Demo Video](https://img.youtube.com/vi/GwMovMFEOwg/0.jpg)](https://youtu.be/GwMovMFEOwg)

## Features

- 🤖 AI-powered Irish music generation
- 📝 Interactive sheet music visualization
- 🔊 Real-time audio playback
- 🎹 Support for multiple musical instruments
- 🎼 ABC notation support
- 🎯 Customizable music parameters

## Project Structure

```
music-copilot/
├── abcsonification/    # ABC notation to audio conversion
├── promptparser/       # Natural language prompt processing
├── sounds_current/     # Generated audio files
├── tunesformer/        # Music generation model
├── main.py            # Main Streamlit application
└── README.md          # Project documentation
```

## Prerequisites

- Conda (Miniconda or Anaconda)
- Python 3.x
- SF2 soundfont file

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd music-copilot
```

2. Create and activate the conda environment:
```bash
conda env create -f musiccopilot.yml
conda activate musiccopilot
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

1. Open your web browser and navigate to the provided local URL

2. Use the sidebar to:
   - Enter your natural language prompt for music generation
   - Modify the transformer prompt if needed
   - Click "Generate Music" to create new music

3. View the generated:
   - Sheet music visualization
   - ABC notation
   - Audio playback

Note: Model Weights and sample Soundfont files available upon request.

## Features in Detail

### Music Generation
- Generate Irish music based on natural language descriptions
- Support for multiple sections and musical parameters
- Customizable key signatures and time signatures

### Visualization
- Real-time sheet music display
- ABC notation editor
- Interactive music playback

### Audio Processing
- High-quality sound synthesis
- Support for multiple instruments
- Real-time audio playback

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.