import React, { forwardRef, useImperativeHandle } from "react";
import { Unity, useUnityContext } from "react-unity-webgl";

const UnityGame = forwardRef((props, ref) => {
  const attack = props.attack;
  const { unityProvider, sendMessage } = useUnityContext({
    loaderUrl: "unitybuild/build.loader.js",
    dataUrl: "unitybuild/build.data",
    frameworkUrl: "unitybuild/build.framework.js",
    codeUrl: "unitybuild/build.wasm",

    symbolsUrl: "unitybuild/build.symbols.json",
    streamingAssetsUrl: "StreamingAssets",
    companyName: "DefaultCompany",
    productName: "3D_test",
    productVersion: "0.1",
  });

  function sendAttack() {
    console.log("공격 신호 받아서 유니티로 보낸다");
    sendMessage("Player1(Clone)", "Attack");
  }

  useImperativeHandle(ref, () => ({
    sendAttack,
  }));

  return (
    <div>
      <Unity
        unityProvider={unityProvider}
        style={{ width: 900, height: 600 }}
      />
    </div>
  );
});
export default UnityGame;
