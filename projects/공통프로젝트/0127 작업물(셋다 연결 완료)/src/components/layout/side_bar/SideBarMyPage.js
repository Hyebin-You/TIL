import BadgeModal from './BadgeModal';
import FriendListModal from './FriendListModal';
import './SideBar.module.css';
import { Link } from "react-router-dom";
// import Button from '../../UI/Button';

// 사이드바는 로비, 게시판에 있을 경우 (유저프로필, 방 생성, 친구 목록, 랭킹) 이 표시되고,
//            마이페이지에 있을 경우 (유저 프로필 + 경험치 바, 뱃지 목록, 친구 목록, 회원정보 수정, 회원 탈퇴)가 표시된다.
const SideBar = () => {

  return (
    <aside>
      <p>
        로비 페이지의 사이드 바입니다.
      </p>

      {/* 유저 프로필 */}
      <p>
        유저의 정보가 표시됩니다.
        <Link to="/mypage/dongsum">LV.25 정동섬</Link>
      </p>

      {/* 뱃지 모달 */}
      <BadgeModal />

      {/* 친구 목록 모달 */}
      <FriendListModal />
      
      {/* 회원정보 페이지로 이동 */}
      <button>
        <Link to="/update" >회원정보 수정</Link>
      </button>

      {/* 회원 탈퇴 페이지로 이동 */}
      <button>
        <Link to="/delete" >회원 탈퇴</Link>
      </button>



      


    </aside>
  );
};

export default SideBar;
;
