import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from 'react'
import type { CategoryId } from '@/lib/tarot'
import type { TarotCardMeta } from '@/lib/tarot-cards'

export type Language = 'en' | 'ko' | 'ja' | 'zh'

export const LANGUAGES: Array<{
  code: Language
  label: string
  nativeLabel: string
  flag: string
}> = [
  { code: 'en', label: 'English', nativeLabel: 'English', flag: '🇺🇸' },
  { code: 'ko', label: 'Korean', nativeLabel: '한국어', flag: '🇰🇷' },
  { code: 'ja', label: 'Japanese', nativeLabel: '日本語', flag: '🇯🇵' },
  { code: 'zh', label: 'Chinese', nativeLabel: '中文', flag: '🇨🇳' },
]

const STORAGE_KEY = 'pirot-language'

const copy: Record<Language, Record<string, string>> = {
  en: {
    language: 'Language',
    cardBackAlt: 'Tarot card back',
    carouselAria: 'Sample tarot card 3D carousel',
    selectCardAria: 'Card {n}',
    piPayment: 'Pi payment',
    heroBadge: 'AI tarot with Pi Coin',
    heroLine1: "Today\u2019s fate,",
    heroLine2: 'with PI-rot',
    heroBody:
      'Choose from 78 mystical cards yourself. AI reads each selected card with care. Pay simply with Pi Coin.',
    startReading: 'Start tarot reading',
    priceHint: 'From 1π · Results in under a minute',
    carouselCaption:
      'Generated PI tarot cards · Hover to pause the carousel',
    howItWorks: 'How it works',
    footer: 'PI-rot · AI tarot service for the Pi Coin community',
    step1Title: 'Choose topic & pay',
    step1Desc:
      'From today\u2019s fortune to a full reading. Pay easily with Pi Coin.',
    step2Title: 'Select cards',
    step2Desc: 'Pick the cards that call to you from the 78-card deck.',
    step3Title: 'AI reading',
    step3Desc: 'AI reads your cards and returns a personal interpretation.',
    categoriesTitle: 'What story do you want to explore?',
    categoriesDesc:
      'The number of cards and Pi price change by reading topic.',
    cardsUnit: 'cards',
    paymentTitle: 'Payment',
    paymentDesc: 'Pay safely with Pi Coin and start your reading.',
    paymentTopic: 'Topic',
    paymentCardCount: 'Cards',
    paymentNetworkFee: 'Network fee',
    paymentTotal: 'Total',
    wallet: 'Pi wallet',
    balance: 'Balance',
    connected: 'Connected',
    paymentSafety: 'Payment is handled securely through Pi Network.',
    payButton: 'Pay {amount} π',
    paymentProcessing: 'Approving payment...',
    paymentDone: 'Payment complete',
    selectTitle: 'Choose your cards',
    scrollSpreadHint: 'Scroll to browse the spread',
    selectDescPrefix: 'Clear your mind and choose ',
    selectDescSuffix: ' card(s) that feel right.',
    selectionComplete: 'Selection complete',
    remainingCards: '{count} more to choose',
    confirmResult: 'View result',
    confirmRemaining: 'Choose {count} more card(s)',
    loadingTitle: 'AI is reading your cards',
    loading1: 'Reading the energy of the cards...',
    loading2: 'Checking the stars...',
    loading3: 'Weaving your story...',
    loading4: 'Your message will arrive soon.',
    resultBadge: '{category} reading result',
    resultTitle: 'Your cards have been revealed',
    resultCardHint: 'Place your hand on a card to see it larger.',
    summaryTitle: 'Overall reading',
    detailAdviceTitle: 'PI-rot advice',
    home: 'Home',
    restart: 'Try again',
    categoryTodayName: "Today\u2019s fortune",
    categoryTodayTagline: 'A single message to open your day',
    categoryLoveName: 'Love & compatibility',
    categoryLoveTagline: 'The flow of connection and the heart',
    categoryMoneyName: 'Money & wealth',
    categoryMoneyTagline: 'Read the energy of money and opportunity',
    categoryCareerName: 'Career & work',
    categoryCareerTagline: 'At the crossroads of work and growth',
    categoryOverallName: 'Full life reading',
    categoryOverallTagline: 'A deeper reading across your whole life',
    positionOne: "Today\u2019s message",
    positionPast: 'Past · Cause',
    positionPresent: 'Present · Situation',
    positionFuture: 'Future · Flow',
    positionCore: 'Core',
    positionObstacle: 'Obstacle',
    positionConclusion: 'Conclusion',
    positionNth: 'Card {n}',
    summary:
      'For this {category} reading, you are entering a gentle period of transition. The cards suggest that you already know the answer and can trust your intuition.',
    advice:
      'Focus on one small decision today. Instead of waiting for the perfect moment, take one step toward where your heart is pointing.',
    readingText:
      '{card} carries the energy of “{keyword}”. In the {position} position, this card asks you to pause and feel the flow. You do not need to rush; the path is already opening.',
    keyword0: 'New beginning',
    keyword1: 'The grace of waiting',
    keyword2: 'Courage and decision',
    keyword3: 'Inner voice',
    keyword4: 'Abundant harvest',
    keyword5: 'Relationship shift',
    keyword6: 'Finding balance',
    keyword7: 'Hidden opportunity',
    keyword8: 'Healing and recovery',
    keyword9: 'Signal of intuition',
    keyword10: 'Reward of patience',
    keyword11: 'Wind of change',
  },
  ko: {
    language: '언어',
    cardBackAlt: '타로 카드 뒷면',
    carouselAria: '예시 타로 카드 3D 캐러셀',
    selectCardAria: '카드 {n}',
    piPayment: 'Pi 결제',
    heroBadge: '파이코인으로 만나는 AI 타로',
    heroLine1: '오늘의 운명을,',
    heroLine2: 'PI-rot 에게',
    heroBody:
      '78장의 신비로운 카드 속에서 당신이 직접 고른 카드를, AI가 한 장 한 장 정성껏 풀이해 드립니다. 결제는 파이코인으로 간편하게.',
    startReading: '타로 보기 시작',
    priceHint: '1회 1π 부터 · 1분 안에 결과 확인',
    carouselCaption:
      '실제 생성된 PI 타로 카드 · 마우스를 올리면 잠시 멈춰요',
    howItWorks: '이렇게 진행돼요',
    footer: 'PI-rot · 파이코인 커뮤니티를 위한 AI 타로 서비스',
    step1Title: '주제 선택 & 결제',
    step1Desc: '오늘의 운세부터 종합 리딩까지. 파이코인으로 간편하게 결제해요.',
    step2Title: '카드 선택',
    step2Desc: '78장의 카드 속에서 마음이 이끄는 카드를 직접 뽑습니다.',
    step3Title: 'AI 풀이',
    step3Desc: 'AI가 뽑힌 카드를 읽고 당신만을 위한 해석을 들려드려요.',
    categoriesTitle: '어떤 이야기가 궁금하세요?',
    categoriesDesc: '주제에 따라 뽑는 카드 수와 결제 금액이 달라져요.',
    cardsUnit: '장',
    paymentTitle: '결제하기',
    paymentDesc: '파이코인으로 안전하게 결제하고 리딩을 시작하세요.',
    paymentTopic: '주제',
    paymentCardCount: '카드 수',
    paymentNetworkFee: '네트워크 수수료',
    paymentTotal: '총 결제금액',
    wallet: 'Pi 지갑',
    balance: '잔액',
    connected: '연결됨',
    paymentSafety: '결제 정보는 Pi Network 위에서 안전하게 처리됩니다.',
    payButton: '{amount} π 결제하기',
    paymentProcessing: '결제 승인 중...',
    paymentDone: '결제 완료',
    selectTitle: '카드를 선택하세요',
    scrollSpreadHint: '펼쳐진 카드를 좌우로 둘러보세요',
    selectDescPrefix: '마음을 비우고, 끌리는 카드 ',
    selectDescSuffix: '을 골라주세요.',
    selectionComplete: '선택 완료!',
    remainingCards: '{count}장 더 선택',
    confirmResult: '결과 확인하기',
    confirmRemaining: '{count}장 더 선택해주세요',
    loadingTitle: 'AI가 카드를 풀이하고 있어요',
    loading1: '카드의 기운을 읽고 있어요...',
    loading2: '별들의 위치를 살피는 중...',
    loading3: '당신의 이야기를 엮고 있어요...',
    loading4: '곧 운명의 메시지가 도착합니다.',
    resultBadge: '{category} 리딩 결과',
    resultTitle: '당신을 위한 카드가 펼쳐졌어요',
    resultCardHint: '카드에 손을 올리면 더 크게 볼 수 있어요.',
    summaryTitle: '종합 풀이',
    detailAdviceTitle: 'PI-rot 의 조언',
    home: '홈으로',
    restart: '다시 보기',
    categoryTodayName: '오늘의 운세',
    categoryTodayTagline: '하루를 여는 단 한 장의 메시지',
    categoryLoveName: '연애 · 궁합',
    categoryLoveTagline: '인연의 흐름과 마음의 방향',
    categoryMoneyName: '금전 · 재물',
    categoryMoneyTagline: '돈의 기운과 기회를 읽다',
    categoryCareerName: '진로 · 직업',
    categoryCareerTagline: '일과 성장의 갈림길에서',
    categoryOverallName: '종합 운세',
    categoryOverallTagline: '삶 전체를 아우르는 깊은 리딩',
    positionOne: '오늘의 메시지',
    positionPast: '과거 · 원인',
    positionPresent: '현재 · 상황',
    positionFuture: '미래 · 흐름',
    positionCore: '핵심',
    positionObstacle: '장애물',
    positionConclusion: '결론',
    positionNth: '{n}번째 카드',
    summary:
      '{category} 리딩 결과, 전체적으로 부드러운 전환의 시기에 들어서 있습니다. 카드들은 당신이 이미 답을 알고 있으며, 그 직관을 믿어도 좋다고 이야기합니다.',
    advice:
      '오늘은 작은 결정 하나에 집중해 보세요. 완벽한 때를 기다리기보다, 마음이 향하는 곳으로 한 걸음 내딛는 것이 가장 좋은 선택이 됩니다.',
    readingText:
      '{card} 카드는 “{keyword}”의 기운을 담고 있어요. {position}에서 이 카드는 지금 당신에게 멈춰 서서 흐름을 느껴보라 말합니다. 서두르지 않아도 길은 이미 열려 있습니다.',
    keyword0: '새로운 시작',
    keyword1: '기다림의 미학',
    keyword2: '용기와 결단',
    keyword3: '내면의 목소리',
    keyword4: '풍요로운 결실',
    keyword5: '관계의 전환',
    keyword6: '균형 잡기',
    keyword7: '숨겨진 기회',
    keyword8: '치유와 회복',
    keyword9: '직관의 신호',
    keyword10: '인내의 보상',
    keyword11: '변화의 바람',
  },
  ja: {
    language: '言語',
    cardBackAlt: 'タロットカードの裏面',
    carouselAria: 'サンプルタロットカード3Dカルーセル',
    selectCardAria: 'カード{n}',
    piPayment: 'Pi決済',
    heroBadge: 'Piコインで出会うAIタロット',
    heroLine1: '今日の運命を、',
    heroLine2: 'PI-rotへ',
    heroBody:
      '78枚の神秘的なカードからあなたが選んだカードを、AIが一枚ずつ丁寧に読み解きます。支払いはPiコインで簡単に。',
    startReading: 'タロットを始める',
    priceHint: '1回1πから · 1分以内に結果確認',
    carouselCaption:
      '生成済みPIタロットカード · ホバーで一時停止',
    howItWorks: '流れ',
    footer: 'PI-rot · PiコインコミュニティのためのAIタロットサービス',
    step1Title: 'テーマ選択 & 決済',
    step1Desc: '今日の運勢から総合リーディングまで。Piコインで簡単決済。',
    step2Title: 'カード選択',
    step2Desc: '78枚の中から心が惹かれるカードを選びます。',
    step3Title: 'AIリーディング',
    step3Desc: 'AIが選ばれたカードを読み、あなた専用の解釈を返します。',
    categoriesTitle: 'どんな物語を知りたいですか？',
    categoriesDesc: 'テーマによってカード枚数と料金が変わります。',
    cardsUnit: '枚',
    paymentTitle: '決済',
    paymentDesc: 'Piコインで安全に支払い、リーディングを始めましょう。',
    paymentTopic: 'テーマ',
    paymentCardCount: 'カード数',
    paymentNetworkFee: 'ネットワーク手数料',
    paymentTotal: '合計金額',
    wallet: 'Piウォレット',
    balance: '残高',
    connected: '接続済み',
    paymentSafety: '決済情報はPi Network上で安全に処理されます。',
    payButton: '{amount} πを支払う',
    paymentProcessing: '承認中...',
    paymentDone: '決済完了',
    selectTitle: 'カードを選んでください',
    scrollSpreadHint: '左右にスクロールしてカードを見てください',
    selectDescPrefix: '心を静めて、惹かれるカードを',
    selectDescSuffix: '選んでください。',
    selectionComplete: '選択完了',
    remainingCards: 'あと{count}枚選択',
    confirmResult: '結果を見る',
    confirmRemaining: 'あと{count}枚選んでください',
    loadingTitle: 'AIがカードを読み解いています',
    loading1: 'カードの気配を読んでいます...',
    loading2: '星の位置を確かめています...',
    loading3: 'あなたの物語を紡いでいます...',
    loading4: 'まもなくメッセージが届きます。',
    resultBadge: '{category}の結果',
    resultTitle: 'あなたのカードが開かれました',
    resultCardHint: 'カードに手を置くと大きく見ることができます。',
    summaryTitle: '総合リーディング',
    detailAdviceTitle: 'PI-rotからのアドバイス',
    home: 'ホームへ',
    restart: 'もう一度',
    categoryTodayName: '今日の運勢',
    categoryTodayTagline: '一日を始める一枚のメッセージ',
    categoryLoveName: '恋愛・相性',
    categoryLoveTagline: '縁の流れと心の方向',
    categoryMoneyName: '金運・財運',
    categoryMoneyTagline: 'お金の流れと機会を読む',
    categoryCareerName: '仕事・キャリア',
    categoryCareerTagline: '仕事と成長の分岐点で',
    categoryOverallName: '総合運',
    categoryOverallTagline: '人生全体を見渡す深いリーディング',
    positionOne: '今日のメッセージ',
    positionPast: '過去・原因',
    positionPresent: '現在・状況',
    positionFuture: '未来・流れ',
    positionCore: '核心',
    positionObstacle: '障害',
    positionConclusion: '結論',
    positionNth: '{n}枚目のカード',
    summary:
      '{category}のリーディングでは、穏やかな転換期に入っていることが示されています。カードは、あなたがすでに答えを知っており、その直感を信じてよいと伝えています。',
    advice:
      '今日は小さな決断ひとつに集中してみましょう。完璧な時を待つより、心が向かう場所へ一歩進むことが良い選択になります。',
    readingText:
      '{card}は「{keyword}」のエネルギーを持っています。{position}の位置で、このカードは立ち止まり流れを感じるよう語りかけています。急がなくても道はすでに開いています。',
    keyword0: '新しい始まり',
    keyword1: '待つことの美しさ',
    keyword2: '勇気と決断',
    keyword3: '内なる声',
    keyword4: '豊かな実り',
    keyword5: '関係の転換',
    keyword6: 'バランス',
    keyword7: '隠れた機会',
    keyword8: '癒しと回復',
    keyword9: '直感のサイン',
    keyword10: '忍耐の報酬',
    keyword11: '変化の風',
  },
  zh: {
    language: '语言',
    cardBackAlt: '塔罗牌背面',
    carouselAria: '示例塔罗牌3D轮播',
    selectCardAria: '第{n}张牌',
    piPayment: 'Pi 支付',
    heroBadge: '用 Pi 币体验 AI 塔罗',
    heroLine1: '今天的命运，',
    heroLine2: '交给 PI-rot',
    heroBody:
      '从78张神秘卡牌中亲自选择你的牌，AI会逐张细致解读。使用Pi币即可轻松支付。',
    startReading: '开始塔罗',
    priceHint: '每次1π起 · 1分钟内查看结果',
    carouselCaption:
      '已生成的PI塔罗牌 · 悬停可暂停',
    howItWorks: '流程',
    footer: 'PI-rot · 面向Pi币社区的AI塔罗服务',
    step1Title: '选择主题并支付',
    step1Desc: '从今日运势到综合解读，使用Pi币轻松支付。',
    step2Title: '选择卡牌',
    step2Desc: '从78张牌中选择最吸引你的卡牌。',
    step3Title: 'AI解读',
    step3Desc: 'AI读取你抽到的牌，并给出专属解释。',
    categoriesTitle: '你想了解什么故事？',
    categoriesDesc: '不同主题对应不同抽牌数量和价格。',
    cardsUnit: '张',
    paymentTitle: '支付',
    paymentDesc: '使用Pi币安全支付并开始解读。',
    paymentTopic: '主题',
    paymentCardCount: '卡牌数',
    paymentNetworkFee: '网络手续费',
    paymentTotal: '总金额',
    wallet: 'Pi 钱包',
    balance: '余额',
    connected: '已连接',
    paymentSafety: '支付信息将在Pi Network上安全处理。',
    payButton: '支付 {amount} π',
    paymentProcessing: '正在确认支付...',
    paymentDone: '支付完成',
    selectTitle: '请选择卡牌',
    scrollSpreadHint: '左右滚动浏览展开的卡牌',
    selectDescPrefix: '清空思绪，选择',
    selectDescSuffix: '最吸引你的牌。',
    selectionComplete: '选择完成',
    remainingCards: '还需选择{count}张',
    confirmResult: '查看结果',
    confirmRemaining: '请再选择{count}张',
    loadingTitle: 'AI正在解读卡牌',
    loading1: '正在读取卡牌能量...',
    loading2: '正在确认星辰位置...',
    loading3: '正在编织你的故事...',
    loading4: '命运讯息即将到达。',
    resultBadge: '{category}解读结果',
    resultTitle: '你的卡牌已经展开',
    resultCardHint: '把手放在卡牌上即可放大查看。',
    summaryTitle: '综合解读',
    detailAdviceTitle: 'PI-rot 的建议',
    home: '回首页',
    restart: '重新开始',
    categoryTodayName: '今日运势',
    categoryTodayTagline: '开启一天的一张讯息',
    categoryLoveName: '恋爱 · 合盘',
    categoryLoveTagline: '关系的流向与内心方向',
    categoryMoneyName: '金钱 · 财富',
    categoryMoneyTagline: '读取财富能量与机会',
    categoryCareerName: '事业 · 工作',
    categoryCareerTagline: '站在工作与成长的岔路口',
    categoryOverallName: '综合运势',
    categoryOverallTagline: '覆盖人生整体的深度解读',
    positionOne: '今日讯息',
    positionPast: '过去 · 原因',
    positionPresent: '现在 · 状况',
    positionFuture: '未来 · 流向',
    positionCore: '核心',
    positionObstacle: '阻碍',
    positionConclusion: '结论',
    positionNth: '第{n}张牌',
    summary:
      '{category}解读显示，你正进入一段温和的转变期。卡牌提示你其实已经知道答案，可以相信自己的直觉。',
    advice:
      '今天请专注于一个小决定。与其等待完美时机，不如朝着内心指向的地方迈出一步。',
    readingText:
      '{card}带有“{keyword}”的能量。在{position}位置上，这张牌提醒你停下来感受流动。不必急躁，道路已经慢慢打开。',
    keyword0: '新的开始',
    keyword1: '等待的美感',
    keyword2: '勇气与决断',
    keyword3: '内在声音',
    keyword4: '丰盛收获',
    keyword5: '关系转变',
    keyword6: '取得平衡',
    keyword7: '隐藏机会',
    keyword8: '疗愈与恢复',
    keyword9: '直觉信号',
    keyword10: '耐心的回报',
    keyword11: '变化之风',
  },
}

const categoryKeys: Record<CategoryId, string> = {
  today: 'categoryToday',
  love: 'categoryLove',
  money: 'categoryMoney',
  career: 'categoryCareer',
  overall: 'categoryOverall',
}

const majorNames: Record<Language, string[]> = {
  en: [],
  ko: [
    '바보',
    '마법사',
    '여사제',
    '여황제',
    '황제',
    '교황',
    '연인',
    '전차',
    '힘',
    '은둔자',
    '운명의 수레바퀴',
    '정의',
    '매달린 사람',
    '죽음',
    '절제',
    '악마',
    '탑',
    '별',
    '달',
    '태양',
    '심판',
    '세계',
  ],
  ja: [
    '愚者',
    '魔術師',
    '女教皇',
    '女帝',
    '皇帝',
    '教皇',
    '恋人',
    '戦車',
    '力',
    '隠者',
    '運命の輪',
    '正義',
    '吊るされた男',
    '死神',
    '節制',
    '悪魔',
    '塔',
    '星',
    '月',
    '太陽',
    '審判',
    '世界',
  ],
  zh: [
    '愚者',
    '魔术师',
    '女祭司',
    '皇后',
    '皇帝',
    '教皇',
    '恋人',
    '战车',
    '力量',
    '隐者',
    '命运之轮',
    '正义',
    '倒吊人',
    '死神',
    '节制',
    '恶魔',
    '高塔',
    '星星',
    '月亮',
    '太阳',
    '审判',
    '世界',
  ],
}

const suitNames: Record<Language, Record<string, string>> = {
  en: { wands: 'Wands', cups: 'Cups', swords: 'Swords', pentacles: 'Pentacles' },
  ko: { wands: '완드', cups: '컵', swords: '소드', pentacles: '펜타클' },
  ja: { wands: 'ワンド', cups: 'カップ', swords: 'ソード', pentacles: 'ペンタクル' },
  zh: { wands: '权杖', cups: '圣杯', swords: '宝剑', pentacles: '星币' },
}

const rankNames: Record<Language, Record<string, string>> = {
  en: {},
  ko: {
    Ace: '에이스',
    Two: '2',
    Three: '3',
    Four: '4',
    Five: '5',
    Six: '6',
    Seven: '7',
    Eight: '8',
    Nine: '9',
    Ten: '10',
    Page: '페이지',
    Knight: '기사',
    Queen: '퀸',
    King: '킹',
  },
  ja: {
    Ace: 'エース',
    Two: '2',
    Three: '3',
    Four: '4',
    Five: '5',
    Six: '6',
    Seven: '7',
    Eight: '8',
    Nine: '9',
    Ten: '10',
    Page: 'ペイジ',
    Knight: 'ナイト',
    Queen: 'クイーン',
    King: 'キング',
  },
  zh: {
    Ace: '王牌',
    Two: '二',
    Three: '三',
    Four: '四',
    Five: '五',
    Six: '六',
    Seven: '七',
    Eight: '八',
    Nine: '九',
    Ten: '十',
    Page: '侍从',
    Knight: '骑士',
    Queen: '王后',
    King: '国王',
  },
}

type I18nContextValue = {
  language: Language
  setLanguage: (language: Language) => void
  hasSelectedLanguage: boolean
  t: (key: string, params?: Record<string, string | number>) => string
}

const I18nContext = createContext<I18nContextValue | null>(null)

function normalizeLanguage(value: string | null): Language {
  return value === 'ko' || value === 'ja' || value === 'zh' || value === 'en'
    ? value
    : 'en'
}

export function I18nProvider({ children }: { children: ReactNode }) {
  const storedLanguage = localStorage.getItem(STORAGE_KEY)
  const [language, setLanguageState] = useState<Language>(() =>
    normalizeLanguage(storedLanguage),
  )
  const [hasSelectedLanguage, setHasSelectedLanguage] = useState(
    () => storedLanguage !== null,
  )

  useEffect(() => {
    document.documentElement.lang = language
  }, [language])

  const value = useMemo<I18nContextValue>(() => {
    function setLanguage(nextLanguage: Language) {
      setLanguageState(nextLanguage)
      setHasSelectedLanguage(true)
      localStorage.setItem(STORAGE_KEY, nextLanguage)
    }

    function t(key: string, params: Record<string, string | number> = {}) {
      let template = copy[language][key] ?? copy.en[key] ?? key
      for (const [param, value] of Object.entries(params)) {
        template = template.replaceAll(`{${param}}`, String(value))
      }
      return template
    }

    return {
      language,
      setLanguage,
      hasSelectedLanguage,
      t,
    }
  }, [hasSelectedLanguage, language])

  return <I18nContext.Provider value={value}>{children}</I18nContext.Provider>
}

export function useI18n() {
  const context = useContext(I18nContext)
  if (!context) throw new Error('useI18n must be used within I18nProvider')
  return context
}

export function getCategoryCopy(
  language: Language,
  id: CategoryId | null | undefined,
) {
  if (!id) return null
  const key = categoryKeys[id]
  return {
    name: copy[language][`${key}Name`] ?? copy.en[`${key}Name`],
    tagline: copy[language][`${key}Tagline`] ?? copy.en[`${key}Tagline`],
  }
}

export function positionLabels(language: Language, count: number): string[] {
  const t = copy[language]
  if (count === 1) return [t.positionOne]
  if (count === 3) return [t.positionPast, t.positionPresent, t.positionFuture]
  if (count === 5)
    return [t.positionCore, t.positionObstacle, t.positionPast, t.positionFuture, t.positionConclusion]
  return Array.from({ length: count }, (_, i) =>
    t.positionNth.replace('{n}', String(i + 1)),
  )
}

export function localizeCardName(card: TarotCardMeta | undefined, language: Language) {
  if (!card) return ''
  if (language === 'en') return card.name
  if (card.arcana === 'major') {
    return majorNames[language][card.id] ?? card.kr ?? card.name
  }
  const rank = card.rank ? rankNames[language][card.rank] ?? card.rank : ''
  const suit = card.suit ? suitNames[language][card.suit] ?? card.suit : ''
  if (language === 'zh') return `${suit}${rank}`
  return `${suit} ${rank}`.trim()
}

export function keyword(language: Language, index: number) {
  return copy[language][`keyword${index}`] ?? copy.en[`keyword${index}`]
}
