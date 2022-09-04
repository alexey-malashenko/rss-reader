"""The module is intended for converting feeds fo html or pdf"""

import os
import weasyprint
from jinja2 import Environment, FileSystemLoader
from .logger import logging_dec, parameter_log


log = parameter_log()


@logging_dec
def converter(config, full_lst, path_html_tmpl, path_to_html, path_to_pdf):
    """Define the converted

        Returns:

        """

    if not full_lst:
        log.info('Got empty full_list: {}'.format(''))
        return

    html_rss = convert_to_html(full_lst, path_html_tmpl)
    save_to(config, html_rss, path_to_html, path_to_pdf)


@logging_dec
def convert_to_html(full_lst, path_html_tmpl):
    """Define the convert to html

        Returns:
            converted html
        """

    file_loader = FileSystemLoader(path_html_tmpl)
    env = Environment(loader=file_loader)
    template = env.get_template(os.path.basename('html_tmp.html'))

    if full_lst:
        output = template.render(html_rss=full_lst)

        return output
    else:
        pass


@logging_dec
def save_to(config, html_rss, path_to_html, path_to_pdf):
    """Define the saving to html or pdf file

        Returns:

        """

    if config['to_html']:
        # logging.info('Converting to html')
        with open(path_to_html, 'w') as file:
            file.writelines(html_rss)
        log.info('Writing to html: successful{}'.format(''))

    if config['to_pdf']:
        # logging.info('Converting to pdf')
        weasyprint.HTML(string=html_rss).write_pdf(path_to_pdf)
        log.info('Writing to pdf: successful{}'.format(''))
