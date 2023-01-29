import React, { forwardRef, useImperativeHandle } from "react";
import { Unity, useUnityContext } from "react-unity-webgl";

const UnityGame = forwardRef((props, ref) => {
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

  // useEffect(() => {
  //   unityProvider.on("canvas", (canvas) => {
  //     canvas.width = 1000;
  //     canvas.height = 700;
  //   });
  // }, []);

  return (
    <div>
      <Unity
        unityProvider={unityProvider}
        matchWebGLToCanvasSize={false}
        className="unityGame"
      />
    </div>
  );
});
export default UnityGame;
