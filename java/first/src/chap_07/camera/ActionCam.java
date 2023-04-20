package chap_07.camera;

public final class ActionCam extends Camera {
    public final String lens; // = "광각렌즈";
    // 선언과 동시에 할당해도 되고 아니면 할당은 생성자에서 해도 됨
    public ActionCam() {
        super("액션 카메라");
        lens = "광곽렌즈";
    }

    public final void makeVideo() {
        System.out.println(this.name + " : " + this.lens +"로 촬영한 영상을 통해 멋진 비디오를 제작합니다.");
    }
}
