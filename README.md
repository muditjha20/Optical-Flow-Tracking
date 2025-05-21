Optical Flow Tracking using OpenCV

Project Overview  
This project implements real-time optical flow tracking using OpenCV and Python. It detects key points in a video stream and tracks their movement across frames using the Lucas-Kanade Optical Flow algorithm. The system dynamically refreshes key points and visualizes object motion with motion trails.

Features  
- Real-time motion tracking using optical flow  
- Automatic keypoint detection with Shi-Tomasi Corner Detection  
- Motion trails visualization to highlight object movement  
- Frame rate (FPS) display for performance monitoring  
- Clear trails feature (press 'C' to reset tracking)  

Installation  
Make sure you have Python installed (Python 3.6+ recommended). Then install the required dependencies:

pip install opencv-python numpy  

How to Run  
1. Clone this repository or download the script:  

   git clone https://github.com/yourusername/Optical-Flow-Tracking.git  
   cd Optical-Flow-Tracking  

2. Run the script:  

   python optical_flow.py  

3. Move objects in front of your webcam and see the motion tracking in action!  

Controls  
- Press 'Q' → Exit the program  
- Press 'C' → Clear motion trails and restart tracking  

Example Output  
![Optical Flow Example](https://via.placeholder.com/600x300)  
How It Works  
1. Detects keypoints in the first frame using Shi-Tomasi Corner Detection  
2. Tracks movement of these keypoints across frames using Lucas-Kanade Optical Flow  
3. Draws motion trails to visualize movement patterns  
4. Refreshes keypoints if tracking becomes sparse  
5. Displays FPS for performance monitoring  

Technologies Used  
- Python  
- OpenCV  
- NumPy  

Future Improvements  
- Enhance tracking with Deep Learning-based Optical Flow (e.g., Farneback, DeepFlow)  
- Improve keypoint robustness using feature descriptors (e.g., ORB, SIFT)  
- Implement object detection alongside tracking  

👨‍💻 Author 
Mudit Mayank Jha
📧 Contact: [muditjha1404@gmail.com](mailto:muditjha1404@gmail.com)  
🌐 GitHub: [muditjha20](https://github.com/muditjha20)
