/*
A P5JS script to illustrate the creation of a basic squiggly line drawn
using the beginShape(), curveVertex(), and endShape() functions.

@author - https://github.com/alphazwest
@version - 9/30/2021
 */

// Define global variables
let segments;
let length;
let x;
let y;
let yRand;
let points;

/**
 * Primary initialization function called once.
 */
function setup() {

    // Create the canvas object on which all
    // drawings are rendered (html canvas element)
    createCanvas(512, 512);

    // Constrain our lines to 3/4 canvas size
    length = width * 0.75;

    // Define segments
    segments = 6;

    // Define starting points (middle of canvas, with some padding)
    x = length / segments;
    y = height * 0.5;
}

/**
 * Primary Processing function called during each frame.
 */
function draw() {

    // Redraw the background each frame
    background("#efefef");

    // Loop through creating line segments
    beginShape()
    noFill()

    // Add the first point
    stroke('black')
    strokeWeight(5)
    curveVertex(x, y)
    curveVertex(x, y)  // duplicate start point

    // Save points for visualization later
    let points = [{x: x, y: y}] //<----- Add initial point here

    // Draw line
    for (let i = 0; i < segments; i++){

        // Get random y
        yRand = random(-(height * 0.125), height * 0.125);

        // Add point to curve
        curveVertex(x += length / segments, y += yRand);

        // Save point
        points.push({x: x, y: y})

    }
    vertex(x, y)  // Duplicate ending point
    endShape()

    // Draw points for visualization
    stroke('#ff9900')
    strokeWeight(10)
    points.push({x: x, y: y})
    points.forEach(function(p){
        point(p.x, p.y)
    })

    // Draw the line once and stop
    noLoop();
}
