import React, { useRef, useEffect } from "react";
import * as tf from "@tensorflow/tfjs";
import * as handpose from "@tensorflow-models/handpose";
import Webcam from "react-webcam";
import './App.css';
import { drawHand } from "./utilities";


function App() {
    //Be able to pass references to other functions
    const webcamRef = useRef(null);
    const canvasRef = useRef(null);
    //const connect = window.drawConnectors;
    var camera = null;

    //Running the handpose model - Function
    const runHandpose = async() => {
        //Neural network
        const net = await handpose.load();
        console.log("Handpose model loaded");
        //Detection hands function trough loop - set interval Js function
        setInterval(() => {
            detect(net);
        }, 100); //every 100ms detect a hand in the frame
    };

    //Running the hand detection trough camera - Function
    const detect = async(net) => {
        //Checking receiving video feed from webcam
        if (
            typeof webcamRef.current !== "undefined" &&
            webcamRef.current !== null &&
            webcamRef.current.video.readyState === 4
        ) {
            //Get video properties (current reference)
            const video = webcamRef.current.video;
            const videoWidth = webcamRef.current.video.videoWidth;
            const videoHeight = webcamRef.current.video.videoHeight;
            //Set video height and width
            webcamRef.current.video.width = videoWidth;
            webcamRef.current.video.height = videoHeight;
            //Set canvas height and width
            canvasRef.current.width = videoWidth;
            canvasRef.current.height = videoHeight;
            //Make detections - estimate the hand in the frame
            const hand = await net.estimateHands(video);
            console.log(hand);
            //Draw mesh
            const ctx = canvasRef.current.getContext("2d");
            drawHand(hand, ctx);
        }
    };

    runHandpose();

    return ( <
        div className = "App" >
        <
        header className = "App-header" >
        <
        Webcam ref = { webcamRef }
        style = {
            {
                position: "absolute",
                marginLeft: "auto",
                marginRight: "auto",
                left: 0,
                right: 0,
                textAlign: "center",
                zindex: 9,
                width: 640,
                height: 480,
            }
        }
        />

        <
        canvas ref = { canvasRef }
        style = {
            {
                position: "absolute",
                marginLeft: "auto",
                marginRight: "auto",
                left: 0,
                right: 0,
                textAlign: "center",
                zindex: 9,
                width: 640,
                height: 480,
            }
        }
        /> 

        <
        /header> 
        <div class="container">
            <video class="input_video"></video>
            <canvas class="output_canvas" width="640px" height="480px"></canvas>
        </div>
        
        </div>
        
    );
}

export default App;