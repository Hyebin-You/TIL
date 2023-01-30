import classes from "./Lobby.module.css";
import RoomList from "./room_list/RoomList";
import WithNavBarAndSideBar from "../layout/WithNavBarAndSideBar";

const Lobby = () => {
  return (
    <main className={classes.lobby}>
      {/* 방 검색 + 방 목록 */}
      <div className={classes.roomContainer}>
        <form>
          <input type="text" className={classes.roomSearch} />
          <button type="submit">검색</button>
        </form>
        <hr />
        <RoomList />
      </div>
    </main>
  );
};

export default WithNavBarAndSideBar(Lobby);
