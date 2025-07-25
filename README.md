# Road Rush 🏍️

A thrilling endless racing game built with Python and Pygame where you navigate through traffic while trying to achieve the highest speed and distance!

![Road Rush](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-Required-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 Game Features

- **Endless Racing**: Drive as far as you can without crashing
- **Dynamic Speed System**: Accelerate by holding W key, speed automatically decreases over time
- **Smart Traffic**: AI-controlled cars with collision avoidance spawning system
- **Real-time Stats**: Track your current speed, top speed, and distance covered
- **Smooth Controls**: Responsive left/right movement with A/D keys
- **Collision Detection**: Precise collision detection using Pygame masks

## 🚀 How to Play

### Controls
- **A**: Move left
- **D**: Move right  
- **W**: Accelerate (hold to increase speed)
- **ESC**: Quit game

### Objective
- Avoid crashing into other cars
- Try to achieve maximum speed (up to 200)
- Cover the longest distance possible
- Challenge yourself to beat your high score!

## 🛠️ Installation

### Prerequisites
- Python 3.x
- Pygame library

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/road-rush.git
   cd road-rush
   ```

2. Install required dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
RoadRush/
├── main.py                          # Main game loop and initialization
├── Car.py                          # Car class and smart spawning logic
├── Player.py                       # Player vehicle class and controls
├── Road.py                         # Road scrolling system
├── speed_handler.py                # Speed management system
├── player_distance_calculator.py   # Distance tracking system
├── images/                         # Game assets
   ├── bike.png                   # Player vehicle sprite
   ├── car.png                    # Traffic car sprite
   └── road.jpg                   # Road texture

```

## 🎯 Game Mechanics

### Speed System
- Base speed starts low and can be increased by holding the W key
- Speed automatically decreases over time to add challenge
- Maximum achievable speed is 200 units
- Speed affects both player movement and traffic spawn rate

### Smart Traffic Spawning
- Cars spawn at multiple lane positions for variety
- Intelligent collision avoidance prevents cars from spawning too close together
- Spawn rate increases with player speed for added difficulty
- Cars move faster than the road to create realistic traffic flow

### Collision Detection
- Uses Pygame's mask-based collision detection for pixel-perfect accuracy
- Game ends immediately upon collision with any traffic car
- Visual feedback shows current stats before game over

## 🔧 Technical Details

### Key Classes
- **Player**: Handles player vehicle movement and input
- **Car**: Manages traffic vehicles and smart spawning
- **Road**: Creates scrolling road effect
- **Speed Handler**: Manages acceleration and deceleration
- **Distance Calculator**: Tracks player progress

### Performance Optimizations
- Efficient sprite group management
- Automatic cleanup of off-screen objects
- Optimized collision detection
- Smooth 60 FPS gameplay

## 🎨 Assets

The game includes custom sprites for:
- Player motorcycle/bike
- Traffic cars
- Road texture

*Note: Ensure you have the required image files in the `images/` directory before running the game.*

## 🤝 Contributing

Contributions are welcome! Here are some ideas for improvements:

- [ ] Add sound effects and background music
- [ ] Implement power-ups and special abilities
- [ ] Add different vehicle types
- [ ] Create multiple road environments
- [ ] Add high score persistence
- [ ] Implement different difficulty levels
- [ ] Add particle effects for speed boost

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created with ❤️ by [Your Name]

## 🙏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/) - the amazing Python game development library
- Inspired by classic endless runner games
- Thanks to the Python gaming community for inspiration and resources

---

*Enjoy the ride and stay safe on the virtual roads! 🏁*
