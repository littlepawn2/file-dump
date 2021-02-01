PShape pipe, pipe1, pipe2;
int birdy, pipex;
int pipe1y, pipe2y, pipe3y, pipe4y, score;
boolean jump = false, dead = false;


public static boolean dying(int pos, int pipe, int corner, int birdpos) {
  if ((pipe <= pos && pipe > pos-50)) {
    if (birdpos < corner || birdpos > corner + 100) {
      return true;
    }
  }
  return false;
}

public static int add(int score, boolean dead, int pos, int pos2) {
  if (dead == false && pos == pos2) {
    score ++;
  }
  return score;
}




void setup() {
  size(800, 600);
  textSize(40);
  textAlign(CENTER, CENTER);
  
  pipe = createShape(GROUP);
  pipe1 = createShape(RECT, 0, -600, 50, 600);
  pipe1.setFill(color(108, 255, 114));
  pipe2 = createShape(RECT, 0, 120, 50, 600);
  pipe2.setFill(color(108, 255, 114));
  
  pipe.addChild(pipe1);
  pipe.addChild(pipe2);
  
  score = 0;
  birdy = 300;
  pipex = 800;
  pipe1y = int(random(0, 400));
  pipe2y = int(random(0, 400));
  pipe3y = int(random(0, 400));

}

void draw() {
  
  if (!(dead)) {
    background(105, 220, 247);
    
    fill(108, 255, 114);
    rect(0, 550, 800, 50);
    
    
    birdy++;
    birdy++;
    birdy++;
    if (jump) {
      birdy = birdy - 60;
      jump = false;
    }
    fill(250, 231, 83);
    rect(380, birdy, 20, 20);
    
    pipex--;
    pipex--;
    
    if (mousePressed) println(pipex);
    
    if (pipex == -800) {
      pipex = 0;
      pipe2y = pipe3y;
      pipe4y = pipe1y;
      pipe1y = int(random(0, 400));
      pipe3y = int(random(0, 400));
    } 
    
    pushMatrix();
    translate(pipex + 800, pipe1y);
    shape(pipe);
    translate(0, -pipe1y);
    
    translate(-400, pipe2y);
    shape(pipe);
    translate(0, -pipe2y);
    
    translate(800, pipe3y);
    shape(pipe);
    translate(0, -pipe3y);
    
    translate(-1200, pipe4y);
    shape(pipe);
    
    popMatrix();
    
    if (pipex <= 400 && pipex >= 350) {
    dead = dying(400, pipex, pipe4y, birdy);
    score = add(score, dead, pipex, 400);
    } else if (pipex <= 0 && pipex >= -50) {
    dead = dying(0, pipex, pipe2y, birdy);
    score = add(score, dead, pipex, 0);
    } else if (pipex <= -400 && pipex >= -450) {
    dead = dying(-400, pipex, pipe1y, birdy);
    score = add(score, dead, pipex, -400);
    }
    
    text(score, 75, 75);
    
    if (birdy >= 530) {
      dead = true;
    }
  } else {
    text("You died", 400, 300);
  }
  

}

void mousePressed() {
  jump = true;
}

void mouseReleased() {
  jump = false;
}
