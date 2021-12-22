import numpy as np

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat,Command, Itemize, Enumerate, Description, LargeText, \
    SubFigure,LineBreak, VerticalSpace

from pylatex.utils import italic, NoEscape, bold
import os
from pylatex.package import Package
import time

ref_list = ['9.9m_10.0%','10.12m_54.0%','10.25m_90.0%']  #数据文件夹
# id_list = ['PD','peak_rms']  #数据特征
id_list = ['dis_accuracy','dis_precision','ref_accuracy','ref_precision']  #数据特征
summary_folder = '2021-12-20~20-05-49'
figure_suffix = '.png'
summary_s = [summary_folder + '//' + '00hushi---' + i + figure_suffix for i in id_list]
at_original_s = ['2D','1D']
separate_figures = [i + '_' + j + k for i in ref_list for j in id_list for k in at_original_s]
# report_type = '测远'
report_type = '测精准度'
lidar_id = 'AT38CD559038CD55'
lidar_version = '2.6.26fac-2.02b894-203.1.20'
data_source = '\\172.20.2.21\\at\\TestData\\版本测试\\PPV\\基本性能测试\\高低温\\2.6.26fac-2.02b894-203.1.20\\B1-0065\\精准度\\2021-12-18 14-46-55'

if __name__ == '__main__':
    image_filename = os.path.join(os.path.dirname(__file__), 'kitten.jpg')

    geometry_options = {"tmargin": "1cm", "lmargin": "2cm"}
    doc = Document(geometry_options=geometry_options)
    doc.packages.add(Package('ctex'))
    doc.preamble.append(Command('title', 'AT128 B1 ' + report_type + '报告(草稿)'))
    doc.preamble.append(Command('author', '胡石'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    with doc.create(Section('测试结论')):
        with doc.create(Description()) as desc:
            desc.add_item("1）", "测距准度...")
            desc.add_item("2）", "测距精度...")
            desc.add_item("3）", "测反射率准度...")
            desc.add_item("4）", "测反射率精度...")
        with doc.create(Figure(position='h')) as kittens:
            with doc.create(SubFigure(
                    position='h',
                    width=NoEscape(r'0.45\linewidth'))) as left_kitten:
                left_kitten.add_image(summary_s[0],
                                  width=NoEscape(r'\linewidth'),
                                      placement=NoEscape(r'\centering'))
                left_kitten.add_caption('测距准度' + '（文件位置：' + summary_s[0] + ')')
            with doc.create(SubFigure(
                    position='h',
                    width=NoEscape(r'0.45\linewidth'))) as right_kitten:

                right_kitten.add_image(summary_s[1],
                                       width=NoEscape(r'\linewidth'),
                                       placement=NoEscape(r'\centering'))
                right_kitten.add_caption('测距精度' + '（文件位置：' + summary_s[1] + ')')
            # kittens.add_caption("测距精准度")
            doc.append(VerticalSpace("20pt"))
            doc.append(LineBreak())

        # doc.append(bold("\n测反射率精准度"))
        #
        # with doc.create(Figure(position='h!')) as ref_ap_summary:
            with doc.create(SubFigure(
                    position='h',
                    width=NoEscape(r'0.45\linewidth'))) as left_ref_ap_summary:
                left_ref_ap_summary.add_image(summary_s[2],
                                  width=NoEscape(r'\linewidth'),
                                  placement=NoEscape(r'\centering'))
                left_ref_ap_summary.add_caption('测反射率准度' + '（文件位置：' + summary_s[2] + ')')
            with doc.create(SubFigure(
                    position='h',
                    width=NoEscape(r'0.45\linewidth'))) as right_ref_ap_summary:

                right_ref_ap_summary.add_image(summary_s[3],
                                       width=NoEscape(r'\linewidth'),
                                       placement=NoEscape(r'\centering'))
                right_ref_ap_summary.add_caption('测反射率精度' + '（文件位置：' + summary_s[3] + ')')
            kittens.add_caption("测距、测反射率精准度")

    with doc.create(Section('背景')):
        doc.append('B1系列作为AT的一种新型号雷达，版本变更后需要对其在全温度范围的距离、反射率精准度探测性能进行测试。本次测试选用')
        doc.append(italic(lidar_id))
        doc.append('雷达，置于室内恒温设备提供的温度环境中遍历自-30℃到110℃的FPGA温度，对反射率不同的目标板进行距离和反射率的测定。')
    with doc.create(Section('测试方法')):
        with doc.create(Subsection('测试目的')):
            doc.append('测试目的是测试B1雷达在全工作温度范围内的距离反射率性能。由于高低温结合的测试方案还不完善，之前的工作对高温，低温环境下的测试分别采用了两套不同的测试系统，而没有在同一场景下一次性遍历雷达所有工作温度进行测试。另外，本次测试中雷达的最高工作温度达到110℃，故获取的测试数据较以往更多。')
            # doc.append(Math(data=['2*3', '=', 9]))

        with doc.create(Subsection('测试场景')):
            doc.append('本测试环境采用带有压缩机的全自动恒温槽来为雷达提供温度环境。将雷达置于一个贴满保温材料的保温箱中，仅留雷达正前方一处开口用于发射/接受激光信号。保温箱前方放置标定反射率的直板' +
                       '作为测试目标物。为消除温度变化过程中雷达光罩表面的结霜结雾，引入一条高压吹气管道来持续向其表面喷射高速气体。')
            with doc.create(Figure(position='h')) as kitten_pic:
                kitten_pic.add_image(summary_folder + '//' + '流程图.png', width=NoEscape(r'0.9\linewidth'))
                kitten_pic.add_caption('测试场景' + '（文件位置：' + summary_folder + '//' + '流程图.png' + ')')


        with doc.create(Subsection('测试步骤')):
            with doc.create(Description()) as desc:
                desc.add_item("1）", "雷达放置在温槽中，向温槽中持续灌入（高温/低温）循环液体，以给雷达加热/降温。距离雷达10m处分别放置三块不同反射率（10%，54%，90%）的目标板，其法线方向正对雷达")
                desc.add_item("2）", "变温过程中持续用常温气体吹拭雷达外光罩表面，用于除霜或除去水珠")
                desc.add_item("3）", "监控雷达内部温度（FPGA温度），当温度达到指定温度时，测试能打在各反射率目标板上的通道对距离，反射率判断的精准度（当前雷达在温槽中不可俯仰）")
                desc.add_item("4）", "测试温度为雷达FPGA温度 -30℃至110℃")
        with doc.create(Subsection('测试版本')):
            doc.append(italic(lidar_version))
            # with doc.create(Tabular('rc|cl')) as table:
            #     table.add_hline()
            #     table.add_row((1, 2, 3, 4))
            #     table.add_hline(1, 2)
            #     table.add_empty_row()
            #     table.add_row((4, 5, 6, 7))

    a = np.array([[100, 10, 20]]).T
    M = np.matrix([[2, 3, 4],
                   [0, 0, 1],
                   [0, 0, 2]])

    with doc.create(Section('测试数据')):
        doc.append('测试数据地址：')
        doc.append(italic(data_source))
        with doc.create(Subsection('距离精准度随雷达内部温度变化曲线')):
            for ref in ref_list:
                ref_value = '\n' + ref[-5:] + '反射率'
                doc.append(bold(ref_value))
                with doc.create(Figure(position='h!')) as kitten_pic4:
                    kitten_pic4.add_image(summary_folder + '//' + ref[:-1] + '_' + 'dis_accuracy' + '2D.png', width=NoEscape(r'0.8\linewidth'))
                    kitten_pic4.add_caption('准度' + '（文件位置：' + summary_folder + '//' + ref[:-1] + '_' + 'dis_accuracy' + '2D.png' + ')')
                with doc.create(Figure(position='h!')) as kitten_pic4:
                    kitten_pic4.add_image(summary_folder + '//' + ref[:-1] + '_' + 'dis_precision' + '2D.png',
                                          width=NoEscape(r'0.8\linewidth'))
                    kitten_pic4.add_caption('精度' + '（文件位置：' + summary_folder + '//' + ref[:-1] + '_' + 'dis_precision' + '2D.png' + ')')


            # doc.append(Math(data=[Matrix(M), Matrix(a), '=', Matrix(M * a)]))


        # with doc.create(Subsection('Alignat math environment')):
        #     with doc.create(Alignat(numbering=False, escape=False)) as agn:
        #         agn.append(r'\frac{a}{b} &= 0 \\')
        #         agn.extend([Matrix(M), Matrix(a), '&=', Matrix(M * a)])

        # with doc.create(Subsection('Beautiful graphs')):
        #     with doc.create(TikZ()):
        #         plot_options = 'height=4cm, width=6cm, grid=major'
        #         with doc.create(Axis(options=plot_options)) as plot:
        #             plot.append(Plot(name='model', func='-x^5 - 242'))
        #
        #             coordinates = [
        #                 (-4.77778, 2027.60977),
        #                 (-3.55556, 347.84069),
        #                 (-2.33333, 22.58953),
        #                 (-1.11111, -493.50066),
        #                 (0.11111, 46.66082),
        #                 (1.33333, -205.56286),
        #                 (2.55556, -341.40638),
        #                 (3.77778, -1169.24780),
        #                 (5.00000, -3269.56775),
        #             ]
        #
        #             plot.append(Plot(name='estimate', coordinates=coordinates))

        with doc.create(Subsection('（各测试通道统计）测距精准度随雷达内部温度变化曲线')):
            for ref in ref_list:
                ref_value = '\n' + ref[-5:] + '反射率'
                doc.append(bold(ref_value))
                with doc.create(Figure(position='h!')) as kitten_pic4:
                    kitten_pic4.add_image(summary_folder + '//' + ref[:-1] + '_' + 'dis_accuracy' + '1D.png', width=NoEscape(r'0.8\linewidth'))
                    kitten_pic4.add_caption('准度' + '（文件位置：' + summary_folder + '//' + ref[:-1] + '_' + 'dis_accuracy' + '1D.png' + ')')
                with doc.create(Figure(position='h!')) as kitten_pic4:
                    kitten_pic4.add_image(summary_folder + '//' + ref[:-1] + '_' + 'dis_precision' + '1D.png',
                                          width=NoEscape(r'0.8\linewidth'))
                    kitten_pic4.add_caption('精度' + '（文件位置：' + summary_folder + '//' + ref[:-1] + '_' + 'dis_precision' + '1D.png' + ')')
        with doc.create(Subsection('反射率精准随雷达内部温度变化曲线')):
            for ref in ref_list:
                ref_value = '\n' + ref[-5:] + '反射率'
                doc.append(bold(ref_value))
                with doc.create(Figure(position='h!')) as kitten_pic4:
                    kitten_pic4.add_image(summary_folder + '//' + ref[:-1] + '_' + 'ref_accuracy' + '2D.png', width=NoEscape(r'0.8\linewidth'))
                    kitten_pic4.add_caption('准度' + '（文件位置：' + summary_folder + '//' + ref[:-1] + '_' + 'ref_accuracy' + '2D.png' + ')')
                with doc.create(Figure(position='h!')) as kitten_pic4:
                    kitten_pic4.add_image(summary_folder + '//' + ref[:-1] + '_' + 'ref_precision' + '2D.png',
                                          width=NoEscape(r'0.8\linewidth'))
                    kitten_pic4.add_caption('精度' + '（文件位置：' + summary_folder + '//' + ref[:-1] + '_' + 'ref_precision' + '2D.png' + ')')
        with doc.create(Subsection('(各测试通道统计）反射率精准度随雷达内部温度变化曲线)')):
            for ref in ref_list:
                ref_value = '\n' + ref[-5:] + '反射率'
                doc.append(bold(ref_value))
                with doc.create(Figure(position='h!')) as kitten_pic4:
                    kitten_pic4.add_image(summary_folder + '//' + ref[:-1] + '_' + 'ref_accuracy' + '1D.png', width=NoEscape(r'0.8\linewidth'))
                    kitten_pic4.add_caption('准度' + '（文件位置：' + summary_folder + '//' + ref[:-1] + '_' + 'ref_accuracy' + '1D.png' + ')')
                with doc.create(Figure(position='h!')) as kitten_pic4:
                    kitten_pic4.add_image(summary_folder + '//' + ref[:-1] + '_' + 'ref_precision' + '1D.png',
                                          width=NoEscape(r'0.8\linewidth'))
                    kitten_pic4.add_caption('精度' + '（文件位置：' + summary_folder + '//' + ref[:-1] + '_' + 'ref_precision' + '1D.png' + ')')

    doc.generate_pdf('AT128 B1 ' + report_type + '报告（草稿）', clean_tex=False)