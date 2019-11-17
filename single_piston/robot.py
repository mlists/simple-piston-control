import magicbot
import wpilib


class Robot(magicbot.MagicRobot):
    def createObjects(self):
        """Create motors and stuff here"""
        self.gamepad = wpilib.XboxController(0)
        self.piston = wpilib.Solenoid(1)

    def teleopInit(self):
        """Called when teleop starts; optional"""
        self.piston.set(False)

    def teleopPeriodic(self):
        """Called on each iteration of the control loop"""
        if self.gamepad.getAButtonPressed():
            if self.piston.get():
                self.piston.set(False)
            else:
                self.piston.set(True)


if __name__ == "__main__":
    wpilib.run(Robot)