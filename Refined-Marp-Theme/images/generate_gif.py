#!/usr/bin/env python3
"""
生成 Marp PPT 展示页面的 GIF 动图
"""
import os
import io
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright


def capture_slides_to_gif(
    html_path: str,
    output_gif: str = "slideshow.gif",
    duration: int = 2000,  # 每张幻灯片显示时间(毫秒)
    width: int = 1920,
    height: int = 1080,
    scale: float = 0.5,  # 缩放比例，减小文件大小
):
    """
    截取 HTML PPT 的每一页并生成 GIF
    
    Args:
        html_path: HTML 文件路径
        output_gif: 输出 GIF 文件名
        duration: 每张幻灯片显示时间(毫秒)
        width: 视口宽度
        height: 视口高度
        scale: 缩放比例
    """
    # 获取绝对路径
    html_path = Path(html_path).resolve()
    file_url = f"file:///{html_path.as_posix()}"
    
    frames = []
    
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": width, "height": height},
            device_scale_factor=1
        )
        
        # 打开 HTML 文件
        page.goto(file_url)
        page.wait_for_load_state("networkidle")
        
        # 获取总页数
        total_pages = page.evaluate("""
            () => {
                const sections = document.querySelectorAll('section[data-marpit-pagination]');
                if (sections.length > 0) {
                    return parseInt(sections[0].getAttribute('data-marpit-pagination-total')) || sections.length;
                }
                return document.querySelectorAll('svg[data-marpit-svg]').length;
            }
        """)
        
        print(f"检测到 {total_pages} 页幻灯片")
        
        # 等待页面渲染完成
        page.wait_for_timeout(500)
        
        # 截取每一页
        for i in range(total_pages):
            print(f"正在截取第 {i + 1}/{total_pages} 页...")
            
            # 截取当前可见的幻灯片区域
            # 找到当前显示的 SVG
            screenshot_bytes = page.screenshot(
                type="png",
                clip={"x": 0, "y": 0, "width": width, "height": height}
            )
            
            # 转换为 PIL Image
            img = Image.open(io.BytesIO(screenshot_bytes))
            
            # 缩放图片
            if scale != 1.0:
                new_size = (int(width * scale), int(height * scale))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            frames.append(img)
            
            # 导航到下一页（除了最后一页）
            if i < total_pages - 1:
                # 使用键盘右箭头或点击下一页按钮
                page.keyboard.press("ArrowRight")
                page.wait_for_timeout(300)  # 等待动画完成
        
        browser.close()
    
    # 保存为 GIF
    print(f"正在生成 GIF，共 {len(frames)} 帧...")
    
    # 计算每帧持续时间（GIF 使用 1/100 秒为单位）
    gif_duration = duration // 10  # 转换为 1/100 秒
    
    # 保存 GIF
    if frames:
        frames[0].save(
            output_gif,
            save_all=True,
            append_images=frames[1:],
            duration=gif_duration,
            loop=0,  # 无限循环
            optimize=True,
            disposal=2  # 每帧显示后清除
        )
        print(f"GIF 已保存: {output_gif}")
        print(f"文件大小: {os.path.getsize(output_gif) / 1024 / 1024:.2f} MB")
    else:
        print("错误: 没有捕获到任何帧")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) >= 3:
        input_html = sys.argv[1]
        output_gif = sys.argv[2]
    else:
        # 默认值
        input_html = "samples_zh_rmt-dark-blue.html"
        output_gif = "samples_zh_rmt-dark-blue.gif"
    
    capture_slides_to_gif(
        html_path=input_html,
        output_gif=output_gif,
        duration=4000,  # 每页显示 4 秒
        scale=800/1920,  # 缩放到 800x450
    )
