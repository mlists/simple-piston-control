import magicbot
import wpilib


class Robot(magicbot.MagicRobot):
    def createObjects(self):
        """Create motors and stuff here"""
        self.gamepad = wpilib.XboxController(0)
        self.pistons = (wpilib.DoubleSolenoid(1, 4), wpilib.DoubleSolenoid(2, 5), wpilib.DoubleSolenoid(3, 6))

    def teleopInit(self):
        """Called when teleop starts; optional"""
        for piston in self.pistons:
            piston.set(wpilib.DoubleSolenoid.Value.kReverse)

    def teleopPeriodic(self):
        """Called on each iteration of the control loop"""
        if self.gamepad.getAButtonPressed():
            print("here")
            if self.pistons[0].get() == wpilib.DoubleSolenoid.Value.kForward:
                for piston in self.pistons:
                    piston.set(wpilib.DoubleSolenoid.Value.kReverse)
            else:
                for piston in self.pistons:
                    piston.set(wpilib.DoubleSolenoid.Value.kForward)


if __name__ == "__main__":
    wpilib.run(Robot)